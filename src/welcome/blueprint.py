from flask import Blueprint

from src.welcome import controller

welcome_blueprint = Blueprint(
    "welcome_blueprint",
    __name__,
    template_folder="templates",
)

welcome_blueprint.add_url_rule("/", view_func=controller.list_numbers, methods=["GET"])
