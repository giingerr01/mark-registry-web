from app.storage.database import Base, engine
from app.storage.models import MarkDB, StudentDB

Base.metadata.create_all(bind=engine)

print("Students and marks tables are created successfully!")
