import pandas as pd

# Load the dataset
file_path = "./mobile_customers.xlsx"  # Replace with your Excel file path
df = pd.read_excel(file_path)
columnName = "employer"

# Define a function to tokenize employers
def tokenize_employers(column):
    # Get unique employers
    unique_employers = column.unique()

    # Generate unique tokens for each employer
    employer_tokens = {employer: f"EMP_{i:04d}" for i, employer in enumerate(unique_employers, start=1)}

    # Map the tokens back to the column
    return column.map(employer_tokens)

# Apply the tokenization function to the 'employer' column
if columnName in df.columns:
    tokenized_employer_column = tokenize_employers(df[columnName])

# Copy the tokenized column to the clipboard
tokenized_employer_column.to_clipboard(index=False)

print("Tokenized employer Done")
