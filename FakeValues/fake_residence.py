import pandas as pd
from faker import Faker

# Initialize Faker
faker = Faker()

# Load the Excel file
file_path = "./mobile_customers.xlsx"  # Replace with your Excel file path
df = pd.read_excel(file_path)
columnName = "residence"

# Generate fake residence
def fake_residence():
    return faker.city()  # Generates a fake city name

# Replace the 'residence' column with fake values
if columnName in df.columns:
    updated_residence_column = df[columnName].apply(lambda x: fake_residence() if pd.notnull(x) else x)

# Copy the updated column to the clipboard
updated_residence_column.to_clipboard(index=False)
print("Residence Done")
