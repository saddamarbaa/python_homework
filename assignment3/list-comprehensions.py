
# Task 3: List Comprehensions Practice

import csv

# Read the CSV file into a list of lists
with open("../csv/employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

# Create a list of full names, skipping the header
names = [
    row[0] + " " + row[1]
    for row in employees[1:]
]

print(names)

# Create a list containing names with the letter "e"
names_with_e = [
    name
    for name in names
    if "e" in name.lower()
]

print(names_with_e)
