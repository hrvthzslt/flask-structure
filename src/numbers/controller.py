from src.numbers import service


def list_numbers() -> tuple:
    return {"numbers": service.list_numbers()}, 200


def add_number(number: int) -> tuple:
    service.add_number(number)
    return {"numbers": service.list_numbers()}, 201


def handle_value_error(error: ValueError) -> tuple:
    return {"error": str(error)}, 400