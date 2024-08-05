from flask import Blueprint

from src.numbers import controller

numbers_blueprint = Blueprint(
    "number_blueprint",
    __name__,
)

numbers_blueprint.add_url_rule("/", view_func=controller.list_numbers, methods=["GET"])

numbers_blueprint.add_url_rule(
    "/<number>", view_func=controller.add_number, methods=["GET"]
)

numbers_blueprint.register_error_handler(ValueError, controller.handle_value_error)
