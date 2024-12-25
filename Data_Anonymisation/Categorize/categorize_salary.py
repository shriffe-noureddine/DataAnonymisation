import pandas as pd

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "salary"

# Define bins and labels for salary
salary_bins = [0, 20000, 50000, 100000, float('inf')]
salary_labels = ["<20,000", "20,000-50,000", "50,001-100,000", ">100,000"]

# Categorize salary
if columnName in df.columns:
    categorized_salary = pd.cut(df[columnName], bins=salary_bins, labels=salary_labels, right=True)

# Copy the categorized column to the clipboard
categorized_salary.to_clipboard(index=False)

print("Categorized Salary Done")
