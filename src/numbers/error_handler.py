def handle_value_error(error: ValueError) -> tuple:
    return {"error": str(error)}, 400
