from datetime import datetime

from psycopg2 import IntegrityError

from database.tables.messages import Messages


class DTOMessage:
    def __init__(self, db):
        self.db = db

    def result_row_message(self, row):
        return {
            "id": row.id,
            "date": str(row.date),
            "time": str(row.time),
            "message": row.message,
            "messenger_id": row.messenger_id,
            "user_id": row.user_id,
        }

    def get_messages_by_messenger(self, messenger_id: int):
        return self.db.session.query(Messages).filter(Messages.messenger_id == messenger_id).all()

    def get_messages_by_part_message_and_messenger(self, part_message: str, messenger_id: int):
        return self.db.session.query(Messages).filter(Messages.message.like(f"%{part_message}%"),
                                                      Messages.messenger_id == messenger_id).all()

    def delete_message(self, part_message: str, messenger_id: int):
        deleted_count = self.db.session.query(Messages).filter(Messages.message == part_message,
                                                               Messages.messenger_id == messenger_id).delete()
        self.db.session.commit()
        return deleted_count
