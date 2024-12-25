import pandas as pd

# Load the Excel file
file_path = "./mobile_customers.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(file_path)
columnName = "username"

# Function to mask usernames
def mask_username(username):
    if pd.isnull(username) or not isinstance(username, str):  # Handle NaN or non-string values
        return username
    if len(username) <= 2:
        return username  # Do not mask usernames with 2 or fewer characters
    return username[0] + "*" * (len(username) - 2) + username[-1]

# Apply the masking function to the 'username' column
if columnName in df.columns:
    masked_username_column = df[columnName].apply(mask_username)

# Copy the masked username column to the clipboard
masked_username_column.to_clipboard(index=False)

print("Masked usernames Done")
