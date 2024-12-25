import pandas as pd
from faker import Faker

# Initialize Faker
faker = Faker()

# Load the Excel file
file_path = "./mobile_customers.xlsx"  # Replace with your Excel file path
df = pd.read_excel(file_path)
columnName = "address"

# Generate fake address
def fake_address():
    return faker.address().replace("\n", ", ")  # Generates a fake address

# Replace the 'address' column with fake values
if columnName in df.columns:
    updated_address_column = df[columnName].apply(lambda x: fake_address() if pd.notnull(x) else x)

# Copy the updated column to the clipboard
updated_address_column.to_clipboard(index=False)
print("Addresses Done")
