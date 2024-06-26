import json
from typing import Optional

from flask import Blueprint, request

from database.db import db
from database.dto.messenger.select.select import DTOSelectMessenger

messenger_get = Blueprint('messengers-get', __name__)

dto_messenger = DTOSelectMessenger(db)


@messenger_get.route("/by-participants", methods=['GET'])
def get_messenger_by_participants():
    participants = request.args.get('participants')
    return dto_messenger.get_messenger_by_participants(participants)


@messenger_get.route("/by-user", methods=['GET'])
def get_messenger_by_user():
    user = request.args.get('user')
    return dto_messenger.get_messenger_by_user(user)
