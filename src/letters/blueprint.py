from flask import Blueprint

from src.letters import controller

letters_blueprint = Blueprint(
    "letter_blueprint",
    __name__,
)

letters_blueprint.add_url_rule("/", view_func=controller.list_letters, methods=["GET"])

letters_blueprint.add_url_rule(
    "/<letter>", view_func=controller.add_letter, methods=["GET"]
)

letters_blueprint.register_error_handler(ValueError, controller.handle_value_error)
