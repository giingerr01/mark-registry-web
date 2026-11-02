from app.schemas import Student
from app.storage.database import SessionLocal
from app.storage.models import MarkDB, StudentDB


def save_students(students: list[Student]) -> None:
    """Saves the list of students to PostgreSQL (clears and syncs)."""
    db = SessionLocal()
    try:
        # Optional: Clear out old records to match your full-file replacement behavior
        db.query(MarkDB).delete()
        db.query(StudentDB).delete()

        for student in students:
            # 1. Create the student record
            db_student = StudentDB(
                id=student.id, name=student.name, email_id=student.email_id
            )
            db.add(db_student)
            db.flush()  # flushes to generate/assign IDs if needed

            # 2. Create individual mark records linked to this student
            for mark in student.marks:
                db_mark = MarkDB(
                    student_id=db_student.id, subject=mark.subject, score=mark.score
                )
                db.add(db_mark)

        # Commit the transaction to save changes permanently
        db.commit()
    except Exception:
        db.rollback()  # Undo changes if anything fails midway
        raise
    finally:
        db.close()
