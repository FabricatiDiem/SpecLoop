import json
from pathlib import Path
from jsonschema import validate, ValidationError
from specloop.models.manifest import Manifest


def validate_manifest(manifest_path: str, schema_path: str) -> bool:
    """Validate a manifest file against a JSON schema."""
    try:
        with open(manifest_path, "r") as f:
            manifest_data = json.load(f)
        with open(schema_path, "r") as f:
            schema = json.load(f)
        validate(instance=manifest_data, schema=schema)
        return True
    except (ValidationError, json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Validation failed: {e}")
        return False


def get_manifest_from_file(manifest_path: str) -> Manifest:
    """Load a Manifest object from a file."""
    with open(manifest_path, "r") as f:
        data = json.load(f)
    return Manifest(**data)
