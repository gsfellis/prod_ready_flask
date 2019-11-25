from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flask!"


@app.route("/echo/request")
def echo():
    try: 
        text = request.args['text']
    except KeyError:
        return "No 'text' parameter found in request.", 400
    
    return text


@app.route("/echo/number/<int:num>")
def echo_number(num):    
    return f"'{num}' is a {type(num).__name__}"


@app.route("/echo/string/<text>")
def echo_string(text):
    return f"'{text}' is a {type(text).__name__}"


@app.route("/healthcheck")
def healthcheck():
    return jsonify(success=True, message="Ok")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
