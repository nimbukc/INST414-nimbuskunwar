import pandas as pd

# Load New York Times COVID deaths data
deaths_df = pd.read_csv("us-states.csv")

# Optional: load vaccination data
vax_file = "COVID-19_Vaccinations_in_the_United_States,Jurisdiction.csv"
