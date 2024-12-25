import pandas as pd

# Load the dataset
df = pd.read_excel("./mobile_customers.xlsx")
columnName = "age"

# Define bins and labels for age
age_bins = [0, 25, 35, 50, float('inf')]
age_labels = ["18-25", "26-35", "36-50", ">50"]

# Categorize age
if columnName in df.columns:
    categorized_age = pd.cut(df[columnName], bins=age_bins, labels=age_labels, right=True)

# Copy the categorized column to the clipboard
categorized_age.to_clipboard(index=False)

print("Categorized age Done")
