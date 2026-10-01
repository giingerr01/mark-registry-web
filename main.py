from fastapi import FastAPI, HTTPException

from schemas import Student

app = FastAPI()

student_db: list[Student] = []


@app.post("/students/", response_model=Student)
def create_students(student: Student):
    for existing in student_db:
        if existing.id == student.id:
            raise HTTPException(status_code=400, detail="student ID already exists")
    student_db.append(student)
    return student


@app.get("/students/", response_model=list[Student])
def get_all_students():
    return student_db
