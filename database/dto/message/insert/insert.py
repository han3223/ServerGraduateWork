import json
from datetime import datetime

from psycopg2 import IntegrityError

from database.dto.message.message import DTOMessage
from database.models.message import Message
from database.tables.messages import Messages


class DTOInsertMessage(DTOMessage):
    def add_message(self, message: Message):
        new_message = Messages(
            date=datetime.strptime(message.date, "%Y-%m-%d"),
            time=datetime.strptime(message.time.split('.')[0], "%H:%M:%S"),
            message=message.message,
            messenger_id=message.messenger_id,
            user_id=message.user_id
        )

        self.db.session.add(new_message)

        try:
            self.db.session.commit()
            return json.dumps(self.result_row_message(new_message))
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag
