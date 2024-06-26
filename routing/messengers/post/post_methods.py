from flask import Blueprint, request

from database.db import db
from database.dto.messenger.insert.insert import DTOInsertMessenger
from database.models.messenger import Messenger

messenger_post = Blueprint('messengers-post', __name__)

dto_messenger = DTOInsertMessenger(db)


@messenger_post.route("/add", methods=['POST'])
def add_messenger():
    json_data = request.data.decode('utf-8')

    print(str(json_data))

    model_messenger = Messenger.parse_raw(str(json_data))

    return dto_messenger.add_messenger(model_messenger)
