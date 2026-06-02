"""Exercises 7-12: OOP, APIs, logging, collections, and exceptions."""

import logging
from collections import deque
from dataclasses import dataclass
from math import isqrt


logging.basicConfig(
    filename="exercise_logs.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass
class Car:
    make: str
    model: str
    year: int
    _battery_size: int = 0

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def update_battery_size(self, battery_size):
        if battery_size < 0:
            raise ValueError("Battery size cannot be negative.")
        self._battery_size = battery_size

    @property
    def battery_size(self):
        return self._battery_size

    @classmethod
    def calculate_age(cls, year, current_year=2026):
        return current_year - year

    def __str__(self):
        return self.display_info()


class ElectricCar(Car):
    def display_info(self):
        return f"{super().display_info()} with {self.battery_size} kWh battery"


def fetch_posts_sample():
    return [
        {"id": 1, "title": "Clean Python basics"},
        {"id": 2, "title": "OOP makes code reusable"},
    ]


def factorial(number):
    if number < 0:
        raise ValueError("Number must be positive.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_prime(number):
    if number < 2:
        return False
    return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))


def logging_demo():
    messages = [
        (logging.DEBUG, "Debugging details"),
        (logging.INFO, "Process started"),
        (logging.WARNING, "Check this value"),
        (logging.ERROR, "Recoverable error"),
        (logging.CRITICAL, "Critical issue example"),
    ]
    for level, message in messages:
        logging.log(level, message)
    return "Logged messages at DEBUG, INFO, WARNING, ERROR, and CRITICAL levels."


def collection_demo():
    fruits = ["mango", "apple", "banana"]
    fruits.append("grapes")
    fruits.sort()

    fixed_data = ("Python", "Internship", 2026)
    unique_scores = {85, 90, 85, 95}
    profile = {"name": "Alice", "role": "student"}

    stack = []
    stack.append("first")
    stack.append("second")
    popped = stack.pop()

    queue = deque(["task-1", "task-2"])
    queue.append("task-3")
    completed = queue.popleft()

    return {
        "list": fruits,
        "tuple": fixed_data,
        "set": sorted(unique_scores),
        "dictionary": profile,
        "stack_popped": popped,
        "queue_completed": completed,
        "deque_remaining": list(queue),
    }


class InvalidMarksError(Exception):
    pass


def calculate_grade(marks):
    try:
        marks = int(marks)
        if not 0 <= marks <= 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        assert marks >= 0
    except ValueError as error:
        logging.exception("Marks conversion failed")
        raise ValueError("Marks must be an integer.") from error
    finally:
        logging.info("Grade calculation attempted")

    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    return "Needs improvement"


if __name__ == "__main__":
    car = ElectricCar("Tata", "Nexon EV", 2024)
    car.update_battery_size(40)
    print("Exercise 7:", car.display_info(), "Age:", Car.calculate_age(car.year))
    print("Exercise 8:", fetch_posts_sample())
    print("Exercise 8 module functions:", factorial(5), is_prime(29))
    print("Exercise 9:", logging_demo())
    print("Exercise 10:", collection_demo())
    print("Exercise 11:", calculate_grade(88))
    print("Exercise 12: unittest recommendation - test these pure functions with assert/unittest.")
