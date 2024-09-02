from src.unique.adapter import list_all_values

UniqueList = list[str]


def list_unique_values() -> UniqueList:
    all_values = list_all_values()
    all_values = [str(value) for value in all_values]
    unique_list = list(set(all_values))
    unique_list.sort()
    return unique_list
