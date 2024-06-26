import json

from database.dto.file.file import DTOFile
from database.dto.values import Status
from database.tables.files import Files


class DTOSelectFile(DTOFile):
    def get_file(self, id: int):
        file = self.db.session.query(Files).filter(Files.id == id).first()
        result = self.result_row_file(file)
        return Status.EMPTY.value if len(result) == 0 else json.dumps(result)

    def get_file_server(self, id: int):
        return self.db.session.query(Files).filter(Files.id == id).first()

