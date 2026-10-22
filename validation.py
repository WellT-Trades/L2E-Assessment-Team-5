import json
from jsonschema import validate, ValidationError, SchemaError, Draft202012Validator

def is_valid_json(json_text):
    try:
        json.loads(json_text)
        return True
    except json.JSONDecodeError:
        return False

def is_valid_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except (ValidationError, SchemaError):
        return False

def is_schema_definition_valid(schema):
    try:
        Draft202012Validator.check_schema(schema)
        return True
    except SchemaError:
        return False
