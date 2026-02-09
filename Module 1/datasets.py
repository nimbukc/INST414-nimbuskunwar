import pandas as pd

# Load New York Times COVID deaths data
deaths_df = pd.read_csv("us-states.csv")

# Load state population data
pop_df = pd.read_excel("/Users/nimbuskunwar/Documents/Data/statepopulation.xlsx")

# Optional: load vaccination data
vax_file = "COVID-19_Vaccinations_in_the_United_States,Jurisdiction.csv"
try:
    vax_df = pd.read_csv(vax_file)
    print("Vaccination data loaded successfully.")
except FileNotFoundError:
    vax_df = None
    print("Vaccination data not found, skipping this step.")
