from flask import Blueprint

from database.db import db
from database.dto.message.select.select import DTOSelectMessage

message_get = Blueprint('messages-get', __name__)

dto_message = DTOSelectMessage(db)
