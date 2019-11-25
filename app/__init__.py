from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)

    # Register your Blueprints
    from app.echo import echo
    from app.root import root

    app.register_blueprint(echo)
    app.register_blueprint(root)

    return app
