from flask import Blueprint

echo = Blueprint('echo', __name__, url_prefix='/echo')


@echo.route("/number/<int:num>")
def echo_number(num):    
    return f"'{num}' is a {type(num).__name__}"


@echo.route("/string/<text>")
def echo_string(text):
    return f"'{text}' is a {type(text).__name__}"
