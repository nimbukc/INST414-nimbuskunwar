import pandas as pd

# Load New York Times COVID deaths data
deaths_df = pd.read_csv("us-states.csv")

# Load the population data
pop_df = pd.read_csv("statepopulation..xlsx")

# load vaccination data (It was to add this to make it optional)
vax_df = pd.read_csv("COVID-19_Vaccinations_in_the_United_States,Jurisdiction.csv")
