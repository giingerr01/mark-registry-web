import json
from pathlib import Path

from schemas import Student

DATA_FILE = Path(__file__).parent / "data.json"


def load_students() -> list[Student]:
    """reads students from data.json and returns a list of students objects."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            raw_data = json.load(f)
            # parsing raw json dict to pydantic student models
            return [Student(**item) for item in raw_data]
        except json.JSONDecodeError:
            return []
