import json
from validation import (
    is_valid_json,
    is_valid_schema,
    is_schema_definition_valid
)
from flask import Flask, request, jsonify, render_template
from comparison import compare_json
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Invalid JSON request."}), 400


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Request must contain a JSON object."}), 400

    if "original" not in data or "updated" not in data:
        return jsonify({
            "error": "Both 'original' and 'updated' fields are required."
        }), 400

    if not isinstance(data["original"], dict) or not isinstance(data["updated"], dict):
        return jsonify({
            "error": "'original' and 'updated' must be JSON objects."
        }), 400

    changes = compare_json(data["original"], data["updated"])

    return jsonify(changes)


@app.route("/validate", methods=["POST"])
def validate_json():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Request must contain a JSON object."}), 400

    if "json_text" not in data:
        return jsonify({"error": "'json_text' is required."}), 400

    json_text = data["json_text"]

    if not isinstance(json_text, str):
        return jsonify({"error": "'json_text' must be a string."}), 400

    if not is_valid_json(json_text):
        return jsonify({
            "valid": False,
            "message": "Invalid JSON syntax."
        }), 400

    if "schema" not in data:
        return jsonify({
            "valid": True,
            "message": "Valid JSON syntax."
        })

    json_data = json.loads(json_text)
    schema = data["schema"]

    if not isinstance(schema, dict):
        return jsonify({"error": "'schema' must be a JSON object."}), 400

    if not is_schema_definition_valid(schema):
        return jsonify({
            "valid": True,
            "schema_valid": False,
            "message": "Invalid JSON Schema definition."
        }), 400

    if is_valid_schema(json_data, schema):
        return jsonify({
            "valid": True,
            "schema_valid": True,
            "message": "JSON is valid and matches the schema."
        })

    return jsonify({
        "valid": True,
        "schema_valid": False,
        "message": "JSON is valid, but does not match the schema."
    })

if __name__ == "__main__":
    app.run(debug=True)
