from src.numbers.service import numbers_service


def add_number(number: int) -> tuple:
    numbers_service.add_number(number)
    return {"numbers": numbers_service.list_numbers()}, 201
