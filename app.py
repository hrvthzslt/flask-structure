from flask import Flask
from src.common.infrastructure.cache import cache
from src.welcome.blueprint import welcome_blueprint
from src.numbers.blueprint import numbers_blueprint
from src.letters.blueprint import letters_blueprint
from src.unique.blueprint import unique_blueprint


app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(welcome_blueprint, url_prefix="/")
app.register_blueprint(numbers_blueprint, url_prefix="/numbers")
app.register_blueprint(letters_blueprint, url_prefix="/letters")
app.register_blueprint(unique_blueprint, url_prefix="/unique")

if __name__ == "__main__":
    app.run()
