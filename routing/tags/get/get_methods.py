from flask import Blueprint, request

from database.db import db
from database.dto.tag.select.select import DTOSelectTag

tag_get = Blueprint('tags-get', __name__)

dto_tag = DTOSelectTag(db)


@tag_get.route("/get-by-type", methods=['GET'])
def get_tag_by_type():
    type = request.args.get('type')

    return dto_tag.get_tags_by_type(type)

