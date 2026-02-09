import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
deaths_df = pd.read_csv("us-states.csv")

vax_df = pd.read_csv(
    "COVID-19_Vaccinations_in_the_United_States,Jurisdiction.csv",
    low_memory=False
)

pop_df = pd.read_csv(
    "historical_state_population_by_year.csv",
    header=None,
    names=["state_abbr", "year", "population"]
)

# Prepare population data
pop_df = pop_df[pop_df["year"] == 2020]

# Map state abbreviations to full names
state_map = {
    "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California",
    "CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia",
    "HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa",
    "KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland",
    "MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi",
    "MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire",
    "NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina",
    "ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania",
    "RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee",
    "TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington",
    "WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"
}

pop_df["state"] = pop_df["state_abbr"].map(state_map)
pop_df = pop_df[["state", "population"]].dropna()

# Prepare deaths data
deaths_df["date"] = pd.to_datetime(deaths_df["date"])
latest_deaths = deaths_df.sort_values("date").groupby("state").tail(1)
latest_deaths = latest_deaths[["state", "deaths"]]

# Prepare vaccination data
vax_df = vax_df.dropna(subset=["Series_Complete_Pop_Pct"])
latest_vax = vax_df.sort_values("Date").groupby("Location").tail(1)

latest_vax["state"] = latest_vax["Location"].map(state_map)
latest_vax = latest_vax[["state", "Series_Complete_Pop_Pct"]]
latest_vax.columns = ["state", "vaccination_rate"]

# Merge datasets
merged = latest_deaths.merge(pop_df, on="state")
merged = merged.merge(latest_vax, on="state")

# Calculate death rate per 100k
merged["death_rate_per_100k"] = (
    merged["deaths"] / merged["population"]
) * 100000

merged.sort_values("death_rate_per_100k", ascending=False).head(10)
# Rank states by death rate per 100k (highest = rank 1)
merged["death_rate_rank"] = merged["death_rate_per_100k"].rank(
    ascending=False, method="dense"
)
# Sort by highest death rate
ranked = merged.sort_values("death_rate_per_100k", ascending=False)
# Show top 10 states with highest death rates
print(
    ranked[[
        "state",
        "population",
        "deaths",
        "vaccination_rate",
        "death_rate_per_100k"
    ]].head(10)
)
