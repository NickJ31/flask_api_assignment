import numbers

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "My Flask API is working!"


@app.route("/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})


# start the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=5000)


@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "invalid JSON data"}), 400

    numbers = data.get("numbers")

    if not isinstance(numbers, list):
        return jsonify({"error": "Numbers must be a list"}), 400

    if not all(
        isinstance(number, (int, float)) and not isinstance(number, bool)
        for number in numbers
    ):
        return jsonify({"error": "all values must be numbers"}), 400

    total = sum(numbers)

    return jsonify({"sum": total})
