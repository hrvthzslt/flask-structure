from src.letters import service


def list_letters() -> tuple:
    return {"letters": service.list_letters()}, 200


def add_letter(letter: str) -> tuple:
    service.add_letter(letter)
    return {"letters": service.list_letters()}, 201


def handle_value_error(error: ValueError) -> tuple:
    return {"error": str(error)}, 400