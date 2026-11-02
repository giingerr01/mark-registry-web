from app.schemas import Student
from app.storage.database import SessionLocal
from app.storage.models import MarkDB, StudentDB


def save_students(students: list[Student]) -> None:
    """Saves the list of students to PostgreSQL (clears and syncs)."""
    db = SessionLocal()
    try:
        db.query(MarkDB).delete()
        db.query(StudentDB).delete()

        for student in students:
            db_student = StudentDB(
                id=student.id, name=student.name, email_id=student.email_id
            )
            db.add(db_student)
            db.flush()

            for mark in student.marks:
                db_mark = MarkDB(
                    student_id=db_student.id, subject=mark.subject, score=mark.score
                )
                db.add(db_mark)

        # save changes permanently
        db.commit()
    except Exception:
        db.rollback()  # Undo changes if anything fails midway
        raise
    finally:
        db.close()
