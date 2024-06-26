from flask import Blueprint, request

from database.db import db
from database.dto.tag.insert.insert import DTOInsertTag
from database.models.tag import Tag

tag_post = Blueprint('tags-post', __name__)

dto_tag = DTOInsertTag(db)


@tag_post.route("/add", methods=['POST'])
def add_tag():
    json_data = request.data.decode('utf-8')
    model_tag = Tag.parse_raw(str(json_data))
    return dto_tag.add_tag(model_tag)
