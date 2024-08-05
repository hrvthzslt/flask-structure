from typing import Any

from src.numbers import repository


numbers = []


def validate_input(number: Any) -> int:
    valid = number.isdigit()
    if not valid:
        raise ValueError("Invalid input")
    return int(number)


def list_numbers() -> repository.NumberList:
    return repository.list_numbers()


def add_number(number: int) -> None:
    repository.add_number(validate_input(number))
