from typing import Any


def validate_input(number: Any) -> int:
    valid = number.isdigit()
    if not valid:
        raise ValueError("Input is not a number.")
    return int(number)
