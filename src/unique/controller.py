from src.infrastructure.cache import cache
from src.unique import service


@cache.cached(timeout=1)
def list_unique_values() -> tuple:
    return {"unique_values": service.list_unique_values()}, 200
