from src.letters.service import list_letters
from src.numbers.service.numbers_service import list_numbers

ValueList = list[str | int]


def list_all_values() -> ValueList:
    return list_numbers() + list_letters()
