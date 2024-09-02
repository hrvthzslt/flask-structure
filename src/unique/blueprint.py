from flask import Blueprint

from src.unique import controller

unique_blueprint = Blueprint(
    "unique_blueprint",
    __name__,
)

unique_blueprint.add_url_rule(
    "/", view_func=controller.list_unique_values, methods=["GET"]
)
