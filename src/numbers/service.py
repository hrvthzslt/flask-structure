from typing import Any


numbers = []


def validate_input(number: Any) -> int:
    valid = number.isdigit()
    if not valid:
        raise ValueError("Invalid input")
    return int(number)



def list_numbers() -> list:
    return numbers


def add_number(number: int) -> None:
    numbers.append(validate_input(number))
