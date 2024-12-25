import pandas as pd

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "credit_card_security_code"

# Function to mask credit card security codes
def mask_credit_card_security_code(cc_code):
    if pd.isnull(cc_code):  # Handle NaN values
        return cc_code
    cc_code = str(cc_code)  # Ensure the value is treated as a string
    return "***"  # Replace the security code with masked value

# Apply the masking function to the 'credit_card_security_code' column
if columnName in df.columns:
    masked_security_code_column = df[columnName].apply(mask_credit_card_security_code)

# Copy the masked security code column to the clipboard
masked_security_code_column.to_clipboard(index=False)

print("Masked credit card security codes Done")
