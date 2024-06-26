import io
import json
from datetime import datetime

import PyPDF2
import chardet as chardet
from PyPDF2 import PdfReader
from psycopg2 import IntegrityError

from NewNetwork import test
from database.dto.document.document import DTODocument
from database.dto.file.select.select import DTOSelectFile
from database.models.document import Document
from database.tables.documents import Documents


class DTOInsertDocument(DTODocument):
    def add_document(self, document: Document):

        dto_file = DTOSelectFile(self.db)
        file = dto_file.get_file_server(document.file_id)

        # Создаем объект BytesIO для работы с байтами
        pdf_file = io.BytesIO(file.file)

        # Создаем объект PdfReader
        pdf_reader = PdfReader(pdf_file)

        # Получаем количество страниц в PDF
        num_pages = len(pdf_reader.pages)

        # Извлекаем текст из каждой страницы
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        new_document = Documents(
            title=document.title,
            category=document.category,
            file_id=document.file_id,
            date=document.date,
            image=document.image,
            user_id=document.user_id,
            tags=document.tags,
            description=test(text) # test(text)
        )

        self.db.session.add(new_document)

        try:
            self.db.session.commit()
            return json.dumps(self.result_row_document(new_document))
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag
