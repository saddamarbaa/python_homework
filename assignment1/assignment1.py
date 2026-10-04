# Task 1: Hello

def hello():
    return "Hello"


# Task 2: Greet with a Formatted String

def greet(name):
    return (f"Hello, {name}")


# Task 3: Calculator
def calc(value1, value2, operation="multiply"):
    try:
        if operation == "add":
            return value1 + value2

        elif operation == "subtract":
            return value1 - value2

        elif operation == "multiply":
            return value1 * value2

        elif operation == "divide":
            return value1 / value2

        elif operation == "modulo":
            return value1 % value2

        elif operation == "int_divide":
            return value1 // value2

        elif operation == "power":
            return value1 ** value2

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return "You can't multiply those values!"


# for testing purposes
# print(calc(5, 2, "add"))


# Task 4
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)

        elif type == "float":
            return float(value)

        elif type == "str":
            return str(value)

    except ValueError:
        return f"You can't convert {value} into a {type}."


# print(data_type_conversion("12.5", "float"))
# print(data_type_conversion(123, "str"))