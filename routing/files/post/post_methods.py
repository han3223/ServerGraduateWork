from flask import Blueprint, request

from database.db import db
from database.dto.file.insert.insert import DTOInsertFile
from database.models.file import File

file_post = Blueprint('files-post', __name__)

dto_file = DTOInsertFile(db)


@file_post.route("/add", methods=['POST'])
def add_file():
    json_data = request.data
    return dto_file.add_file(json_data)
