from fastapi import APIRouter, HTTPException

from app.schemas import MarkEntry, Student
from app.storage.load_students import load_students
from app.storage.save_students import save_students

# creating a router instance
router = APIRouter()


# home
@router.get("/")
def home():
    return {"message": "welcome to the Mark Registry Web API"}


# shows the list of whole student data in (rollno. - name) format
@router.get("/students/", response_model=list[Student])
def get_all_students():
    return load_students()


# api to create a new student
@router.post("/students/", response_model=Student)
def create_students(student: Student):
    students = load_students()
    for existing in students:
        if existing.id == student.id:
            raise HTTPException(status_code=400, detail="student ID already exists")
    students.append(student)
    save_students(students)
    return student


# api to update or add the mark and subject
@router.put("/students/{id}/marks", response_model=Student)
def add_or_update_mark(id: int, mark: MarkEntry):
    students = load_students()
    for student in students:
        if student.id == id:
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


# api to delete or remove and student by using their roll number
@router.delete("/students/{id}")
def delete_student(id: int):
    # load the existing student list from json
    students = load_students()

    target_student = next((s for s in students if s.id == id), None)
    if not target_student:
        raise HTTPException(status_code=404, detail="Student not found!!")

    updated_students = [s for s in students if s.id != id]

    save_students(updated_students)

    return {"message": f"Student'{target_student.name} (ID: {id} removed successfully"}
