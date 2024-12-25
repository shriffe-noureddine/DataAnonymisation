import pandas as pd
from faker import Faker

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "credit_card_provider"

# Initialize Faker for generating random tokens
faker = Faker()

# Define a function to tokenize credit card providers
def tokenize_credit_card_provider(column):
    # Get unique providers
    unique_providers = column.unique()

    # Generate unique tokens for each unique provider
    provider_tokens = {provider: faker.uuid4()[:8] for provider in unique_providers}

    # Map the tokens back to the column
    return column.map(provider_tokens)

# Apply the tokenization function to the 'credit_card_provider' column
if columnName in df.columns:
    tokenized_provider_column = tokenize_credit_card_provider(df[columnName])

# Copy the tokenized column to the clipboard
tokenized_provider_column.to_clipboard(index=False)

print("Tokenized credit card providers Done")
