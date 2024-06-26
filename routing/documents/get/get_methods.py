from datetime import datetime

from flask import Blueprint, request

from database.db import db
from database.dto.document.select.select import DTOSelectDocument

document_get = Blueprint('documents-get', __name__)

dto_document = DTOSelectDocument(db)


@document_get.route("/get-all", methods=['GET'])
def get_all_document():
    return dto_document.get_all_document()


@document_get.route("/get-by-user-id")
def get_documents_by_user_id():
    user_id = request.args.get('user_id')

    return dto_document.get_documents_by_user_id(int(user_id))


@document_get.route("/get-by-title-category-date-tags", methods=['GET'])
def get_documents_by_title_and_category_and_date_and_tags():
    title = request.args.get('title')
    category = request.args.get('category')
    date_after = request.args.get('dateAfter')
    date_before = request.args.get('dateBefore')
    tags = request.args.get('tags')

    return dto_document.get_documents_by_title_and_category_and_date_and_tags(title,
                                                                              category,
                                                                              date_after,
                                                                              date_before,
                                                                              tags)
