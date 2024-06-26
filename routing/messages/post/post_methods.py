from flask import Blueprint, request
from flask_socketio import emit

from database.db import db
from database.dto.message.insert.insert import DTOInsertMessage
from database.models.message import Message

message_post = Blueprint('messages-post', __name__)

dto_message = DTOInsertMessage(db)


@message_post.route("/add", methods=['POST'])
def add_message():
    json_data = request.data.decode('utf-8')
    model_message = Message.parse_raw(str(json_data))

    result = dto_message.add_message(model_message)

    print(result)

    if result is not None:
        emit('message', result, room=model_message.messenger_id)
        
    return result
