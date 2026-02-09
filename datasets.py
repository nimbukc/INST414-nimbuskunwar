import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
# New York Times COVID deaths data
deaths_df = pd.read_csv("us-states.csv")

# Vaccination data
vax_df = pd.read_csv("COVID-19_Vaccinations_in_the_United_States,Jurisdiction.csv")

# State population data 
pop_df = pd.read_csv("historical_state_population_by_year.csv")

# Clean & prepare population data Keep only 2020 population data
pop_df = pop_df[pop_df["year"] == 2020]

# Remove rows with missing population
pop_df = pop_df.dropna(subset=["population"])

pop_df = pop_df[["state", "population"]]

# Clean & prepare deaths data
# Convert date column to datetime
deaths_df["date"] = pd.to_datetime(deaths_df["date"])

# Keep most recent record for each state
latest_deaths = deaths_df.sort_values("date").groupby("state").tail(1)

latest_deaths = latest_deaths[["state", "deaths"]]

# Clean & prepare vaccination data
# Remove rows with missing vaccination rates
vax_df = vax_df.dropna(subset=["Series_Complete_Pop_Pct"])

# Keep most recent vaccination data for each state
latest_vax = vax_df.sort_values("Date").groupby("Location").tail(1)

latest_vax = latest_vax[["Location", "Series_Complete_Pop_Pct"]]
latest_vax.columns = ["state", "vaccination_rate"]

# Merge datasets
merged = latest_deaths.merge(pop_df, on="state", how="inner")
merged = merged.merge(latest_vax, on="state", how="inner")

# Calculate death rate per 100k
merged["death_rate_per_100k"] = (
    merged["deaths"] / merged["population"]
) * 100000

# View final cleaned data
merged.head()