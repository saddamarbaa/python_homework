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


# Task 5
def grade(*args):
    try:
        total = 0
        count = 0

        for score in args:
            total = total + score
            count = count + 1

        average = total / count

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except TypeError:
        return "Invalid data was provided."

# print(grade(75, 85, 95))


# Task 7
def student_scores(operation, **kwargs):
    if operation == "best":
        best_student = ""
        best_score = -1

        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = name

        return best_student

    elif operation == "mean":
        return sum(kwargs.values()) / len(kwargs)


# Task 8
def titleize(string):
    words = string.split()

    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    for i, word in enumerate(words):
        # First word
        if i == 0:
            words[i] = word.capitalize()

        # Last word
        elif word == words[-1]:
            words[i] = word.capitalize()

        # Little word
        elif word in little_words:
            words[i] = word

        # Everything else
        else:
            words[i] = word.capitalize()

    return " ".join(words)


# Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"

    return result


# Task 10
def pig_latin(string):
    words = string.split()
    result = []

    vowels = "aeiou"

    for word in words:

        # Case 1: word starts with a vowel
        if word[0] in vowels:
            new_word = word + "ay"

        # Case 2: word starts with "qu"
        elif word[0:2] == "qu":
            new_word = word[2:] + "quay"

        # Case 3: word starts with one or more consonants
        else:
            index = 0

            for i, letter in enumerate(word):
                if letter in vowels:
                    index = i
                    break

            new_word = word[index:] + word[:index] + "ay"

        result.append(new_word)

    return " ".join(result)