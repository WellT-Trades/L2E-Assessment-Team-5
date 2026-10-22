def compare_json(original, updated, path=""):
    changes = []

    for key in original:
        current_path = f"{path}.{key}" if path else key

        if key not in updated:
            changes.append({
                "path": current_path,
                "type": "removed",
                "old_value": original[key]
            })

        elif isinstance(original[key], dict) and isinstance(updated[key], dict):
            changes.extend(
                compare_json(original[key], updated[key], current_path)
            )

        elif original[key] != updated[key]:
            changes.append({
                "path": current_path,
                "type": "modified",
                "old_value": original[key],
                "new_value": updated[key]
            })

    for key in updated:
        if key not in original:
            current_path = f"{path}.{key}" if path else key

            changes.append({
                "path": current_path,
                "type": "added",
                "new_value": updated[key]
            })

    return changes

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
    original = {
        "address": {
            "city": "Lagos"
        }
    }

    updated = {
        "address": {
            "city": "Abuja"
        }
    }

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
