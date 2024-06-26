import json

from psycopg2 import IntegrityError

from database.db import db
from database.dto.messenger.messenger import DTOMessenger
from database.models.messenger import Messenger
from database.tables.messengers import Messengers


class DTOInsertMessenger(DTOMessenger):
    def add_messenger(self, messenger: Messenger):
        new_messenger = Messengers(participants=str(messenger.participants))

        self.db.session.add(new_messenger)

        try:
            self.db.session.commit()
            return json.dumps(self.result_row_messenger(new_messenger, None))
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag
