
import json
import pandas as pd
from pathlib import Path


# ==========================================
# TASK 1: Creating and Manipulating DataFrames
# ==========================================

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)
print("\nTask 1 - Original DataFrame:")
print(task1_data_frame)

# Add a Salary column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print("\nTask 1 - DataFrame with Salary:")
print(task1_with_salary)

# Increase Age by 1
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

print("\nTask 1 - Employees One Year Older:")
print(task1_older)

# Save to CSV without the index
task1_older.to_csv("employees.csv", index=False)


# ==========================================
# TASK 2: Loading CSV and JSON Data
# ==========================================

# Read employees.csv
task2_employees = pd.read_csv("employees.csv")

print("\nTask 2 - Employees from CSV:")
print(task2_employees)

# Create additional_employees.json
additional_employees = [
    {
        "Name": "Eve",
        "Age": 28,
        "City": "Miami",
        "Salary": 60000
    },
    {
        "Name": "Frank",
        "Age": 40,
        "City": "Seattle",
        "Salary": 95000
    }
]

with open("additional_employees.json", "w", encoding="utf-8") as file:
    json.dump(additional_employees, file, indent=4)

# Read the JSON file into a DataFrame
json_employees = pd.read_json("additional_employees.json")

print("\nTask 2 - Employees from JSON:")
print(json_employees)

# Combine both DataFrames and reset the index
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print("\nTask 2 - All Employees:")
print(more_employees)


# ==========================================
# TASK 3: Data Inspection
# ==========================================

# Get the first three rows
first_three = more_employees.head(3)

print("\nTask 3 - First Three Employees:")
print(first_three)

# Get the last two rows
last_two = more_employees.tail(2)

print("\nTask 3 - Last Two Employees:")
print(last_two)

# Get the shape (rows, columns)
employee_shape = more_employees.shape

print("\nTask 3 - Employee DataFrame Shape:")
print(employee_shape)

# Display DataFrame information
print("\nTask 3 - DataFrame Information:")
more_employees.info()


# ==========================================
# TASK 4: Data Cleaning
# ==========================================

# Find dirty_data.csv in the assignment folder
# or in the repository's csv folder.
if Path("dirty_data.csv").exists():
    dirty_data_path = Path("dirty_data.csv")
elif Path("../csv/dirty_data.csv").exists():
    dirty_data_path = Path("../csv/dirty_data.csv")
else:
    raise FileNotFoundError(
        "Could not find dirty_data.csv. "
        "Place it in the assignment4 folder or ../csv folder."
    )

# Load the dirty data
dirty_data = pd.read_csv(dirty_data_path)

print("\nTask 4 - Original Dirty Data:")
print(dirty_data)

# Create a copy for cleaning
clean_data = dirty_data.copy()

# Remove duplicate rows
clean_data = clean_data.drop_duplicates()

print("\nTask 4 - After Removing Duplicates:")
print(clean_data)

# Convert Age to numeric
# Invalid or missing values become NaN.
clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)

print("\nTask 4 - Age Converted to Numeric:")
print(clean_data)

# Convert Salary to numeric.
# Replace known placeholders with NaN first.
clean_data["Salary"] = (
    clean_data["Salary"]
    .replace(r"(?i)^\s*(unknown|n/a)\s*$", float("nan"), regex=True)
)

clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)

print("\nTask 4 - Salary Converted to Numeric:")
print(clean_data)

# Fill missing Age values with the mean
clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

# Fill missing Salary values with the median
clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)

print("\nTask 4 - Missing Numeric Values Filled:")
print(clean_data)

# Convert Hire Date to datetime.
# The dates may use different formats.
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format="mixed",
    errors="coerce"
)

print("\nTask 4 - Hire Date Converted to Datetime:")
print(clean_data)

# Remove extra whitespace and convert Name and Department to uppercase
clean_data["Name"] = (
    clean_data["Name"]
    .str.strip()
    .str.upper()
)

clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)

print("\nTask 4 - Final Cleaned Data:")
print(clean_data)
