from flask import Blueprint, request

from database.db import db
from database.dto.file.select.select import DTOSelectFile

file_get = Blueprint('files-get', __name__)

dto_file = DTOSelectFile(db)


@file_get.route("/get", methods=['GET'])
def get_file():
    id = request.args.get('id')

    return dto_file.get_file(int(id))
