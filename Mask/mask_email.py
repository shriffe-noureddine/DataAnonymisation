import pandas as pd

# Load the Excel file
file_path = "./mobile_customers.xlsx"  # Replace with your Excel file path
df = pd.read_excel(file_path)
columnName = "email"

# Function to mask email addresses
def mask_email(email):
    if pd.isnull(email) or not isinstance(email, str):  # Handle NaN or non-string values
        return email
    try:
        local, domain = email.split("@")
        if len(local) > 2:
            masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
        else:
            masked_local = "*" * len(local)
        return f"{masked_local}@{domain}"
    except ValueError:  # If the email doesn't have the "@" symbol
        return email

# Apply the masking function to the 'email' column
if columnName in df.columns:
    masked_email_column = df[columnName].apply(mask_email)

# Copy the masked email column to the clipboard
masked_email_column.to_clipboard(index=False)

print("Masked email addresses Done")
