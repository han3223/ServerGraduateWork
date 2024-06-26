import json
from datetime import datetime

from database.dto.document.document import DTODocument
from database.dto.values import Status
from database.tables.documents import Documents


class DTOSelectDocument(DTODocument):
    def get_all_document(self):
        documents = self.db.session.query(Documents).all()
        result = [self.result_row_document(document) for document in documents]
        return Status.EMPTY.value if len(result) == 0 else json.dumps(result)

    def get_documents_by_user_id(self, user_id: int):
        documents = self.db.session.query(Documents).filter(Documents.user_id == user_id).all()
        result = [self.result_row_document(document) for document in documents]
        return Status.EMPTY.value if len(result) == 0 else result

    def get_documents_by_title_and_category_and_date_and_tags(self, title: str, category: str, date_after: str, date_before: str, tags: str):
        all_documents = self.db.session.query(Documents).all()

        filtered_documents = filter(lambda doc: title.lower() in doc.title.lower(), all_documents)

        if category:
            filtered_documents = filter(lambda doc: doc.category == category, filtered_documents)

        if tags:
            filtered_documents = filter(lambda doc: set(tags).issubset(doc.tags), filtered_documents)

        if date_after is not None:
            filtered_documents = filter(lambda doc: datetime.combine(doc.date, datetime.min.time()) >= datetime.strptime(date_after, "%Y-%m-%d"), filtered_documents)

        if date_before is not None:
            filtered_documents = filter(lambda doc: datetime.combine(doc.date, datetime.min.time()) <= datetime.strptime(date_before, "%Y-%m-%d"), filtered_documents)

        result = [self.result_row_document(document) for document in filtered_documents]

        return Status.EMPTY.value if len(result) == 0 else json.dumps(result)
