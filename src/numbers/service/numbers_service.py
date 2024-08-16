from src.numbers import repository
from src.numbers.service.validator import validate_input


def list_numbers() -> repository.NumberList:
    return repository.list_numbers()


def add_number(number: int) -> None:
    repository.add_number(validate_input(number))
