from comparison import compare_json

def test_modified_value():
    original = {"age": 25}
    updated = {"age": 26}

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "age",
            "type": "modified",
            "old_value": 25,
            "new_value": 26
        }
    ]

def test_added_field():
    original = {"age": 25}
    updated = {"age": 25, "city": "Lagos"}

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "city",
            "type": "added",
            "new_value": "Lagos"
        }
    ]

def test_removed_field():
    original = {"age": 25, "city": "Lagos"}
    updated = {"age": 25}

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "city",
            "type": "removed",
            "old_value": "Lagos"
        }
    ]

def test_nested_modified_value():
    original = {"address": {"city": "Lagos"}}
    updated = {"address": {"city": "Abuja"}}

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "address.city",
            "type": "modified",
            "old_value": "Lagos",
            "new_value": "Abuja"
        }
    ]

def test_added_object():
    original = {"name": "Wellington"}
    updated = {
    "name": "Wellington",
    "address": {
    "city": "Lagos",
    "country": "Nigeria"
    }
    }

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "address",
            "type": "added",
            "new_value": {
                "city": "Lagos",
                "country": "Nigeria"
            }
        }
    ]

def test_removed_object():
    original = {
        "name": "Wellington",
        "address": {
        "city": "Lagos",
        "country": "Nigeria"
        }
        }
    updated = {"name": "Wellington"}

    result = compare_json(original, updated)

    assert result == [
        {
            "path": "address",
            "type": "removed",
            "old_value": {
                "city": "Lagos",
                "country": "Nigeria"
            }
        }
    ]

    