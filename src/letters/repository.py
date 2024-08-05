letters = []

StrList = list[str]


def list_letters() -> StrList:
    return letters


def add_letter(letter: str) -> None:
    letters.append(letter)
