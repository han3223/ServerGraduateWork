from psycopg2 import IntegrityError

from database.dto.profile.profile import DTOProfile
from database.dto.values import Status
from database.tables.profiles import Profiles
from hash.hash_password import HashPassword


class DTOUpdateProfile(DTOProfile):
    def update_personal_name(self, email: str, personal_name: str) -> str:
        result = self.db.session\
            .query(Profiles)\
            .filter(Profiles.email == email)\
            .update({Profiles.personalName: personal_name})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_personal_info(self, email: str, personal_info: str) -> str:
        result = self.db.session\
            .query(Profiles)\
            .filter(Profiles.email == email)\
            .update({Profiles.personalInfo: personal_info})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_number_phone(self, email: str, telephone_number: str) -> str:
        result = self.db.session\
            .query(Profiles)\
            .filter(Profiles.email == email)\
            .update({Profiles.phoneNumber: telephone_number})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_email(self, old_email: str, new_email: str) -> str:
        result = self.db.session\
            .query(Profiles)\
            .filter(Profiles.email == old_email)\
            .update({Profiles.email: new_email})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_password(self, email: str, old_password: str, new_password: str) -> str:
        hashed_old_password = HashPassword.hash_password(old_password.replace(" ", "+"))
        hashed_new_password = HashPassword.hash_password(new_password.replace(" ", "+"))
        result = self.db.session\
            .query(Profiles)\
            .filter(Profiles.email == email, Profiles.password == hashed_old_password)\
            .update({Profiles.password: hashed_new_password})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_tags(self, email: str, tag: str) -> str:
        result = self.db.session.query(Profiles).filter(Profiles.email == email).update({Profiles.tags: tag})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_password_using_phone_number(self, telephone_number: str, new_password: str) -> str:
        hashed_new_password = HashPassword.hash_password(new_password.replace(" ", "+"))
        result = self.db.session.query(Profiles).filter(Profiles.phoneNumber == telephone_number).update(
            {Profiles.password: hashed_new_password})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)

    def update_password_using_email(self, email: str, new_password: str) -> str:
        hashed_new_password = HashPassword.hash_password(new_password.replace(" ", "+"))
        result = self.db.session.query(Profiles).filter(Profiles.email == email).update(
            {Profiles.password: hashed_new_password})

        try:
            self.db.session.commit()
            return Status.ERROR.value if result == 0 else str(result)
        except IntegrityError:
            self.db.session.rollback()
            return str(IntegrityError.diag)
