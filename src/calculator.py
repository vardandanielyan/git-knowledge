"""
Calculator Module - Used for Git Training Exercises
Junior developers can implement missing functions and practice branching/merging.
"""


def add(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Returns the quotient of a and b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def modulo(a: float, b: float) -> float:
    """
    Returns the remainder of dividing a by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot modulo by zero!")
    return a % b

APP_VERSION = "1.0.0"
APP_NAME = "Git"
