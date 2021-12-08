from typing import Any


def validate_unique(key: str, current: dict, value: Any, object_id: str):
    return (object_id is None and current[key] == value) or (not current['id'] == object_id and current[key] == value)
