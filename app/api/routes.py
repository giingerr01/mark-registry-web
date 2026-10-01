from fastapi import APIRouter, HTTPException

from app.schemas import MarkEntry, Student
from app.storage.load_students import load_students
from app.storage.save_students import save_students

# creating a router instance
router = APIRouter()


@router.get("/")
def home():
    return {"message": "welcome to the Mark Registry Web API"}


@router.get("/students/", response_model=list[Student])
def get_all_students():
    return load_students()


@router.post("/students/", response_model=Student)
def create_students(student: Student):
    students = load_students()
    for existing in students:
        if existing.id == student.id:
            raise HTTPException(status_code=400, detail="student ID already exists")
    students.append(student)
    save_students(students)
    return student


@router.put("/students/{student_id}/marks", response_model=Student)
def add_or_update_mark(student_id: int, mark: MarkEntry):
    students = load_students()
    for student in students:
        if student.id == student_id:
            for existing_mark in student.marks:
                if (
                    existing_mark.subject.strip().lower()
                    == mark.subject.strip().lower()
                ):
                    existing_mark.score = mark.score
                    save_students(students)
                    return student
            student.marks.append(mark)
            save_students(students)
            return student
    raise HTTPException(status_code=404, detail="Student not found!")


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    # load the existing student list from json
    students = load_students()

    target_student = next((s for s in students if s.id == student_id), None)
    if not target_student:
        raise HTTPException(status_code=404, detail="Student not found!!")

    updated_students = [s for s in students if s.id != student_id]

    save_students(updated_students)

    return {
        "message": f"Student'{target_student.name} (ID: {student_id} removed successfully"
    }
