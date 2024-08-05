from flask import Blueprint

from numbers import service

numbers_blueprint = Blueprint(
    "number_blueprint",
    __name__,
    template_folder="templates",
)

numbers = []


@numbers_blueprint.route("/", methods=["GET"])
def list() -> tuple:
    service.get_number_list()
    return {"numbers": numbers}, 200


@numbers_blueprint.route("/<number>", methods=["POST", "GET"])
def add(number: int) -> tuple:
    numbers.append(number)
    return {"numbers": numbers}, 201
