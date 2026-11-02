from app.schemas import MarkEntry, Student
from app.storage.database import SessionLocal
from app.storage.models import StudentDB


def load_students() -> list[Student]:
    """Reads students and their marks from PostgreSQL and returns Pydantic models."""
    db = SessionLocal()
    try:
        db_students = db.query(StudentDB).all()

        students = []
        for db_student in db_students:
            # Explicitly map and instantiate MarkEntry models so types match perfectly
            marks_list = [
                MarkEntry(subject=m.subject, score=m.score) for m in db_student.marks
            ]

            students.append(
                Student(
                    # Wrap or cast values if the type checker complains about SQLAlchemy attributes
                    id=int(db_student.id),
                    name=str(db_student.name),
                    email_id=str(db_student.email_id),
                    marks=marks_list,
                )
            )
        return students
    finally:
        db.close()
