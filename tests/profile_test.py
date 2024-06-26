import unittest

from database.db import db
from database.dto.profile.insert.insert import DTOInsertProfile
from database.dto.profile.select.select import DTOSelectProfile
from database.dto.profile.update.update import DTOUpdateProfile
from database.models.profile import Profile


class TestProfile(unittest.TestCase):
    dto_insert_profile = DTOInsertProfile(db)
    # dto_update_profile = DTOUpdateProfile(db)
    # dto_select_profile = DTOSelectProfile(db)

    def test_add(self):

        profile = Profile(
            lastName="Петров",
            firstName="Пётр",
            patronymic="Петрович",
            phoneNumber="81234567890",
            email="peter12@gmail.com",
            password="qwerty123")

        result = self.dto_insert_profile.add_profile(profile=profile)
        self.assertEqual(profile, "")

    def get_by_email(self):
        pass

    def get_by_phone_number(self):
        pass

    def get_by_email_and_password(self):
        pass

    def get_by_personal_name(self):
        pass

    def get_without_passwords(self):
        pass

    def get_by_id_without_password(self):
        pass

    def get_recovery_code_using_last_name_and_phone_number(self):
        pass

    def get_recovery_code_using_last_name_and_email(self):
        pass

    def update_personal_name(self):
        pass

    def update_personal_info(self):
        pass

    def update_phone_number(self):
        pass

    def update_email(self):
        pass

    def update_password(self):
        pass

    def update_tags(self):
        pass

    def update_password_using_phone_number(self):
        pass

    def update_password_using_email(self):
        pass

    def delete_profile(self):
        pass
