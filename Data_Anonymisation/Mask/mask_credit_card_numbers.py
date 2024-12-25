import pandas as pd

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "credit_card_number"

# Function to mask credit card numbers
def mask_credit_card_number(cc_number):
    if pd.isnull(cc_number):  # Handle NaN values
        return cc_number
    cc_number = str(cc_number)  # Ensure the value is treated as a string
    if len(cc_number) < 4:  # Handle short or invalid credit card numbers
        return "****"
    return "**** **** **** " + cc_number[-4:]  # Mask all but the last 4 digits

# Apply the masking function to the 'credit_card_number' column
if columnName in df.columns:
    masked_credit_card_column = df[columnName].apply(mask_credit_card_number)

# Copy the masked credit card column to the clipboard
masked_credit_card_column.to_clipboard(index=False)

print("Masked credit card numbers Done")
