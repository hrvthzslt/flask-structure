from src.letters import repository

letters = []


def validate_input(letter: str) -> str:
    valid = letter.isalnum()
    if not valid:
        raise ValueError("Input is not alphanumeric.")
    return str(letter)


def list_letters() -> repository.StrList:
    return repository.list_letters()


def add_letter(letter: str) -> None:
    repository.add_letter(validate_input(letter))
