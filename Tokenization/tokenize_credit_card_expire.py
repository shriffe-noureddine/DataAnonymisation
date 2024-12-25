import pandas as pd

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "credit_card_expire"

# Define a function to tokenize expiration dates
def tokenize_credit_card_expire(column):
    # Get unique expiration dates
    unique_expires = column.unique()

    # Generate unique tokens for each unique expiration date
    expire_tokens = {expire: f"TOKEN_{i:04d}" for i, expire in enumerate(unique_expires, start=1)}

    # Map the tokens back to the column
    return column.map(expire_tokens)

# Apply the tokenization function to the 'credit_card_expire' column
if columnName in df.columns:
    tokenized_expire_column = tokenize_credit_card_expire(df[columnName])

# Copy the tokenized column to the clipboard
tokenized_expire_column.to_clipboard(index=False)

print("Tokenized credit card expirations Done.")
