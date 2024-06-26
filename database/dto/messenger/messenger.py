import json

from psycopg2 import IntegrityError

from database.dto.profile.profile import DTOProfile
from database.dto.profile.select.select import DTOSelectProfile
from database.tables.messengers import Messengers


class DTOMessenger:
    def __init__(self, db):
        self.db = db

    def result_row_messenger(self, row, messages):
        dto_select_profile = DTOSelectProfile(self.db)
        profiles = [dto_select_profile.get_profile_by_id_without_password_m(int(participant)) for participant in json.loads(row.participants)]

        return {
            "id": row.id,
            "participants": profiles,
            "messages": [] if messages is None else messages
        }

    # def get_messenger_by_id(self, id: int):
    #     return self.db.session.query(Messengers).filter(Messengers.id == id).first()
    #
    # def get_messengers_by_user(self, user: int):
    #     return self.db.session.query(Messengers).filter(Messengers.user == user).all()
    #
    # def get_all_messengers(self):
    #     return self.db.session.query(Messengers).all()
    #
    # def add_messenger(self, messenger):
    #     new_messenger = Messengers(user=messenger["user"], interlocutor=messenger["interlocutor"])
    #     self.db.session.add(new_messenger)
    #
    #     try:
    #         self.db.session.commit()
    #         return new_messenger.id
    #     except IntegrityError:
    #         self.db.session.rollback()
    #         return IntegrityError.diag
    #
    # def delete_messenger(self, user, interlocutor):
    #     deleted_count = self.db.session.query(Messengers).filter(Messengers.user == user,
    #                                                              Messengers.interlocutor == interlocutor).delete()
    #     self.db.session.commit()
    #     return deleted_count
    