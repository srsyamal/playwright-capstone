import json

def load_json(file_path: str) -> dict | list:
    """Load and parse JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def deep_compare_json(actual: dict | list, expected: dict | list, path: str = "root") -> list:
    """
    Recursively compares two JSON structures and returns a list of mismatch messages with exact paths.
    """
    mismatches = []

    if type(actual) != type(expected):
        mismatches.append(f"Type mismatch at {path}: actual {type(actual).__name__}, expected {type(expected).__name__}")
        return mismatches

    if isinstance(actual, dict):
        all_keys = set(actual.keys()).union(set(expected.keys()))
        for key in all_keys:
            current_path = f"{path}.{key}"
            if key not in actual:
                mismatches.append(f"Missing key in actual at {current_path}")
            elif key not in expected:
                mismatches.append(f"Unexpected key in actual at {current_path}")
            else:
                mismatches.extend(deep_compare_json(actual[key], expected[key], current_path))

    elif isinstance(actual, list):
        if len(actual) != len(expected):
            mismatches.append(f"List length mismatch at {path}: actual length {len(actual)}, expected length {len(expected)}")
        for idx, (act_item, exp_item) in enumerate(zip(actual, expected)):
            mismatches.extend(deep_compare_json(act_item, exp_item, f"{path}[{idx}]"))

    else:
        if actual != expected:
            mismatches.append(f"Value mismatch at {path}: actual '{actual}', expected '{expected}'")

    return mismatches