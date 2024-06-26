import json
from typing import Optional, cast

from sqlalchemy import ARRAY, Integer, func, text
from sqlalchemy import or_

from database.dto.message.message import DTOMessage
from database.dto.messenger.messenger import DTOMessenger
from database.dto.profile.profile import DTOProfile
from database.dto.values import Status
from database.models.message import Message
from database.tables.messages import Messages
from database.tables.messengers import Messengers
from database.tables.profiles import Profiles


class DTOSelectMessenger(DTOMessenger):
    def get_messenger_by_participants(self, participants: str) -> str:
        all_messengers = self.db.session.query(Messengers).all()
        result = next((messenger for messenger in all_messengers if set(participants).issubset(messenger.participants)), None)

        if result is None:
            return Status.EMPTY.value
        else:
            dto_message = DTOMessage(self.db)
            messages = self.db.session.query(Messages).join(Messengers).all()
            result_row_message = [dto_message.result_row_message(message) for message in messages]

            return json.dumps(self.result_row_messenger(result, result_row_message))

    def get_messenger_by_user(self, user: str) -> str:
        dto_message = DTOMessage(self.db)
        messengers = self.db.session.query(Messengers).filter(Messengers.participants.like(f'%{user}%')).all()

        messages = self.db.session.query(Messages).join(Messengers).all()
        result_row_message = [dto_message.result_row_message(message) for message in messages]
        result = [self.result_row_messenger(messenger, result_row_message) for messenger in messengers]

        return Status.EMPTY.value if len(result) == 0 else json.dumps(result)


