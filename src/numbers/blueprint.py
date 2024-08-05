from flask import Blueprint

from src.numbers import service


numbers_blueprint = Blueprint(
    "number_blueprint",
    __name__,
    template_folder="templates",
)


@numbers_blueprint.route("/", methods=["GET"])
def list() -> tuple:
    return {"numbers": service.list_numbers()}, 200


@numbers_blueprint.route("/<number>", methods=["POST", "GET"])
def add(number: int) -> tuple:
    service.add_number(number)
    return {"numbers": service.list_numbers()}, 201
