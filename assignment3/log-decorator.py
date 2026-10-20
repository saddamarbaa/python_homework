
# Task 1: Writing and Testing a Decorator

import logging

# Set up logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("./decorator.log", mode="a")
file_handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(file_handler)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")
        logger.info(
            f"positional parameters: {args if args else 'none'}"
        )
        logger.info(
            f"keyword parameters: {kwargs if kwargs else 'none'}"
        )
        logger.info(f"return: {result}")

        return result

    return wrapper


# Task 1: Function with no parameters and no return value
@logger_decorator
def say_hello():
    print("Hello, World!")


# Task 1: Function with variable positional arguments
@logger_decorator
def return_true(*args):
    return True


# Task 1: Function with keyword arguments and no positional arguments
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


# Task 1: Call the three decorated functions
say_hello()
print(return_true(10, 20, 30))
print(return_decorator(name="Sam", age=20))

# Close the file handler
file_handler.close()
