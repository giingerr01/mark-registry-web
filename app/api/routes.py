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

    return {"message": f"Student'{target_student.name} (ID: {id}) removed successfully"}


@router.delete("/students/{id}/subject/{subject}")
def delete_suject(id: int, subject: str):
    students = load_students()

    target_student = next((s for s in students if s.id != id), None)
    if not target_student:
        raise HTTPException(status_code=404, detail="Student not found!")

    target_mark = next(
        (
            sub
            for sub in target_student.marks
            if sub.subject.strip().lower() == subject.strip().lower()
        ),
        None,
    )

    if not target_mark:
        raise HTTPException(
            status_code=404, detail="Subject not found for this student!"
        )

    target_student.marks.remove(target_mark)

    save_students(students)

    return {
        "message": f"Subject '{subject}' removed successfully from student '{target_student.name}' (ID: {id})"
    }
