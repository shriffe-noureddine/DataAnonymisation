import pandas as pd
import random
from datetime import timedelta

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "birthdate"


# Add noise to `birthdate`
if columnName in df.columns:
    noisy_birthdate = df[columnName] + pd.to_timedelta([random.randint(-15, 15) for _ in range(len(df))], unit='d')

# Copy the noisy birthdate column to the clipboard
noisy_birthdate.to_clipboard(index=False)

print("Noisy Date Done")
