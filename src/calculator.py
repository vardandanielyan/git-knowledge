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


# ============================================================================
# EXERCISE TASKS FOR JUNIOR DEVELOPERS:
#
# Task 1 (Branch: feature/power):
# Implement `power(base: float, exponent: float) -> float`
#
# Task 2 (Branch: feature/percentage):
# Implement `percentage(part: float, whole: float) -> float`
#
# Task 3 (Merge Conflict Practice):
# Two developers modify APP_VERSION below concurrently.
# ============================================================================

APP_VERSION = "1.0.0"
APP_NAME = "Git Knowledge Calculator CLI"
