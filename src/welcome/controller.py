from flask import render_template
from src.infrastructure.cache import cache


@cache.cached(timeout=1)
def list_numbers() -> tuple:
    return render_template("index.html"), 200
