import json

from app.schemas import Student
from app.storage.data_file import DATA_FILE

"""saving the students data"""


def save_students(students: list[Student]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        dict_data = [student.model_dump() for student in students]
        json.dump(dict_data, file, indent=4)
