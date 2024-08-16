from flask import Blueprint

from src.numbers.controller import list_controller, add_controller
from src.numbers import error_handler

numbers_blueprint = Blueprint(
    "number_blueprint",
    __name__,
)

numbers_blueprint.add_url_rule(
    "/", view_func=list_controller.list_numbers, methods=["GET"]
)

numbers_blueprint.add_url_rule(
    "/<number>", view_func=add_controller.add_number, methods=["POST"]
)

numbers_blueprint.register_error_handler(ValueError, error_handler.handle_value_error)
