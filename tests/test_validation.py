from validation import (
    is_valid_json,
    is_valid_schema,
    is_schema_definition_valid
)

def test_valid_json():
    json_text = '{"name": "WellT", "age": 25}'

    result = is_valid_json(json_text)

    assert result is True

from validation import is_valid_schema


def test_valid_schema():
    data = {"age": 25}
    schema = {
        "type": "object",
        "properties": {
            "age": {"type": "number"}
        },
        "required": ["age"]
    }

    result = is_valid_schema(data, schema)

    assert result is True


def test_invalid_schema():
    data = {"age": "twenty-five"}
    schema = {
        "type": "object",
        "properties": {
            "age": {"type": "number"}
        },
        "required": ["age"]
    }

    result = is_valid_schema(data, schema)

    assert result is False

def test_missing_required_field():
    data = {"name": "WellT"}

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name", "age"]
    }

    result = is_valid_schema(data, schema)
    
    assert result is False

def test_valid_schema_definition():
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        }
    }

    assert is_schema_definition_valid(schema) is True

def test_invalid_schema_definition():
    schema = {
        "type": "unknown"
    }

    assert is_schema_definition_valid(schema) is False
