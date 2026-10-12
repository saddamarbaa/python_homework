
import csv
import sys
import os
import custom_module
from datetime import datetime


# Task 2: Read a CSV File
def read_employees():
    employee_data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    employee_data["fields"] = row
                else:
                    rows.append(row)

        employee_data["rows"] = rows

    except Exception as e:
        print(e)
        sys.exit(1)

    return employee_data


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employees = read_employees()
employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name
def first_name(row_index):
    return employees["rows"][row_index][column_index("first_name")]


# Task 5: Find the Employee
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]
        )
    )
    return matches


# Task 7: Sort the Rows by last_name
def sort_by_last_name():
    employees["rows"].sort(
        key=lambda row: row[column_index("last_name")]
    )
    return employees["rows"]


# Task 8: Create a Dictionary for an Employee
def employee_dict(row):
    result = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[index]

    return result


# Task 9: Create a Dictionary of All Employees
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)

    return result


# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Create and Use Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_one_minutes_file(filename):
        minutes = {}
        rows = []

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    minutes["fields"] = row
                else:
                    rows.append(tuple(row))

        minutes["rows"] = rows
        return minutes

    minutes1 = read_one_minutes_file("../csv/minutes1.csv")
    minutes2 = read_one_minutes_file("../csv/minutes2.csv")

    return minutes1, minutes2


# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)


# Task 14: Convert to datetime
def create_minutes_list():
    rows = list(minutes_set)

    converted_rows = list(
        map(
            lambda x: (
                x[0],
                datetime.strptime(x[1], "%B %d, %Y")
            ),
            rows
        )
    )

    return converted_rows


# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_rows = list(
        map(
            lambda row: (
                row[0],
                datetime.strftime(row[1], "%B %d, %Y")
            ),
            minutes_list
        )
    )

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_rows)

    return converted_rows


# Run the tasks and create the global variables
sort_by_last_name()

print("Employee dictionary:")
print(employee_dict(employees["rows"][0]))

print("All employees:")
print(all_employees_dict())

minutes1, minutes2 = read_minutes()
minutes_set = create_minutes_set()
minutes_list = create_minutes_list()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)
print("Minutes set:", minutes_set)
print("Minutes list:", minutes_list)

set_that_secret("my_new_secret")
print("Custom module secret:", custom_module.secret)

write_sorted_list()