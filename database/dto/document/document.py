from datetime import datetime

from psycopg2 import IntegrityError

from database.tables.documents import Documents


class DTODocument:
    def __init__(self, db):
        self.db = db

    def result_row_document(self, row):
        return {
            "id": row.id,
            "title": row.title,
            "category": row.category,
            "file_id": row.file_id,
            "date": str(row.date),
            "image": str(row.image),
            "user_id": row.user_id,
            "tags": row.tags,
            "description": row.description,
        }
