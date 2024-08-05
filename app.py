from flask import Flask
from src.infrastructure.cache import cache
from src.numbers.blueprint import numbers_blueprint
from src.letters.blueprint import letters_blueprint


app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(numbers_blueprint, url_prefix="/numbers")
app.register_blueprint(letters_blueprint, url_prefix="/letters")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
