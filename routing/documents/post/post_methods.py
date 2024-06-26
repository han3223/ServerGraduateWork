from flask import Blueprint, request

from database.db import db
from database.dto.document.insert.insert import DTOInsertDocument
from database.models.document import Document

document_post = Blueprint('documents-post', __name__)

dto_document = DTOInsertDocument(db)


@document_post.route("/add", methods=['POST'])
def add_document():
    json_data = request.data.decode('utf-8')
    model_document = Document.parse_raw(str(json_data))
    return dto_document.add_document(model_document)
