from flask import Blueprint, jsonify

root = Blueprint('root', __name__)


@root.route("/")
def index():
    return "Hello, Flask!"


@root.route("/healthcheck")
def healthcheck():
    return jsonify(success=True, message="Ok")
