import pandas as pd

# Load the dataset
file_path = "./mobile_customers.xlsx"  # Replace with your Excel file path
df = pd.read_excel(file_path)
columnName = "job"

# Define a function to tokenize jobs
def tokenize_jobs(column):
    # Get unique jobs
    unique_jobs = column.unique()

    # Generate unique tokens for each job
    job_tokens = {job: f"JOB_{i:04d}" for i, job in enumerate(unique_jobs, start=1)}

    # Map the tokens back to the column
    return column.map(job_tokens)

# Apply the tokenization function to the 'job' column
if columnName in df.columns:
    tokenized_job_column = tokenize_jobs(df[columnName])

# Copy the tokenized column to the clipboard
tokenized_job_column.to_clipboard(index=False)

print("Tokenized job data Done")
