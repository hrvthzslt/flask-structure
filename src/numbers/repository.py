numbers = []

NumberList = list[int]


def list_numbers() -> NumberList:
    return numbers


def add_number(number: int) -> None:
    numbers.append(number)
