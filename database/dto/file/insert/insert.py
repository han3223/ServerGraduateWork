import json
from psycopg2 import IntegrityError

from database.dto.file.file import DTOFile
from database.models.file import File
from database.tables.files import Files


class DTOInsertFile(DTOFile):
    def add_file(self, file: bytes):
        new_file = Files(file=file)
        self.db.session.add(new_file)

        try:
            self.db.session.commit()
            return json.dumps(self.result_row_file(new_file))
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag