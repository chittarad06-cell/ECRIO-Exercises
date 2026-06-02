"""Exercises 1-4: Python basics, data types, functions, and control flow."""


def exercise_1_hello_world():
    return "Hello, World!"


def exercise_2_data_types(name="Alice", age="20"):
    age = int(age)
    colors = ["Red", "Green", "Yellow"]
    colors[0] = "Blue"
    numbers = (4, 7, 10)
    product = numbers[0] * numbers[1]
    remainder = 25 % 4
    repeated_word = "Python" * 3

    values = {
        "message": f"Hello {name}, in 5 years you will be {age + 5} years old!",
        "second_color": colors[1],
        "colors": colors,
        "numbers": numbers,
        "product": product,
        "remainder": remainder,
        "repeated_word": repeated_word,
    }
    values["types"] = {key: type(value).__name__ for key, value in values.items()}
    return values


def add_numbers(first, second=0):
    return first + second


def square(number):
    return number * number


square_lambda = lambda number: number * number


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def greet_many_times(name, times=3):
    return [f"Welcome, {name}!" for _ in range(times)]


def exercise_3_functions():
    unpacked_numbers = [10, 20]
    return {
        "positional_sum": add_numbers(5, 7),
        "keyword_sum": add_numbers(first=8, second=9),
        "default_sum": add_numbers(15),
        "unpacked_sum": add_numbers(*unpacked_numbers),
        "square_function": square(6),
        "square_lambda": square_lambda(6),
        "factorial": factorial(5),
        "greetings": greet_many_times("Intern", 2),
    }


def classify_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 18:
        return "minor"
    if age < 60:
        return "adult"
    return "senior"


def multiplication_table(limit=5):
    return [[row * column for column in range(1, limit + 1)] for row in range(1, limit + 1)]


def exercise_4_control_flow(age=22):
    numbers = list(range(1, 16))
    return {
        "age_group": classify_age(age),
        "can_vote": age >= 18,
        "even_numbers": [number for number in numbers if number % 2 == 0],
        "break_example": [number for number in range(1, 21) if number <= 10],
        "continue_example": [number for number in numbers if number % 2 == 0],
        "table_1_to_5": multiplication_table(5),
        "range_1_to_10": list(range(1, 11)),
    }


if __name__ == "__main__":
    print("Exercise 1:", exercise_1_hello_world())
    print("Exercise 2:", exercise_2_data_types("Chittara", "20"))
    print("Exercise 3:", exercise_3_functions())
    print("Exercise 4:", exercise_4_control_flow(20))
