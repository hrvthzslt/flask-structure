from src.numbers.service import numbers_service
from src.infrastructure.cache import cache


@cache.cached(timeout=1)
def list_numbers() -> tuple:
    return {"numbers": numbers_service.list_numbers()}, 200
