import base64

from psycopg2 import IntegrityError

from database.tables.files import Files


class DTOFile:
    def __init__(self, db):
        self.db = db

    def result_row_file(self, row):
        return {
            "id": row.id,
            "file": base64.b64encode(row.file).decode('utf-8')
        }

