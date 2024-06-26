from sqlalchemy.exc import IntegrityError

from database.tables.tags import Tags


class DTOTag:
    def __init__(self, db):
        self.db = db

    def result_row_tag(self, row):
        return {
            "id": row.id,
            "title": row.title,
            "type": row.type
        }
