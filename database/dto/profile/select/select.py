import json
import random

from database.dto.profile.profile import DTOProfile
from database.dto.values import Status
from database.tables.profiles import Profiles
from hash.hash_password import HashPassword


class DTOSelectProfile(DTOProfile):
    def select_profile_by_email(self, email: str) -> str:
        profile = self.db.session.query(Profiles).filter(Profiles.email == email).first()

        return Status.EMPTY.value if profile is None else Status.OK.value

    def select_profile_by_phone_number(self, telephone_number: str) -> str:
        profile = self.db.session.query(Profiles).filter(Profiles.phoneNumber == telephone_number).first()

        return Status.EMPTY.value if profile is None else Status.OK.value

    def select_profile_by_email_and_password(self, email: str, password: str) -> str:
        hashed_password = HashPassword.hash_password(password.replace(" ", "+"))
        profile = self.db.session.query(Profiles).filter(Profiles.email == email,
                                                         Profiles.password == hashed_password).first()

        return Status.EMPTY.value if profile is None else json.dumps(self.result_row_profile(profile))

    def select_profile_by_personal_name(self, personal_name: str):
        profile = self.db.session.query(Profiles).filter(Profiles.personalName == personal_name).first()
        return Status.EMPTY.value if profile is None else json.dumps(self.result_row_profile(profile))

    def select_all_profiles_without_password(self):
        profiles = self.db.session.query(Profiles).all()
        result = [self.result_row_without_password_profile(profile) for profile in profiles]
        return Status.EMPTY.value if len(result) == 0 else result

    def get_profile_by_id_without_password(self, profile_id: int):
        profile = self.db.session.query(Profiles).filter(Profiles.id == profile_id).first()
        return Status.EMPTY.value if profile is None else json.dumps(self.result_row_without_password_profile(profile))

    def get_profile_by_id_without_password_m(self, profile_id: int):
        profile = self.db.session.query(Profiles).filter(Profiles.id == profile_id).first()
        return Status.EMPTY.value if profile is None else self.result_row_without_password_profile(profile)

    def get_recovery_code_using_last_name_and_phone_number(self, last_name: str, telephone_number: str) -> str:
        profile = self.db.session.query(Profiles).filter(Profiles.lastName == last_name,
                                                         Profiles.phoneNumber == telephone_number).first()

        return Status.EMPTY.value if not profile else str(random.randint(1000, 9999))

    def get_recovery_code_using_last_name_and_email(self, last_name: str, email: str):
        profile = self.db.session.query(Profiles).filter(Profiles.lastName == last_name,
                                                         Profiles.email == email).first()
        return Status.EMPTY.value if not profile else str(random.randint(1000, 9999))

    def get_profiles_by_name_personal_name_tags(self, name: str, tags: str):
        filtered_profiles = self.db.session.query(Profiles).all()

        if len(name) != 0:
            if name[0] == "@":
                filtered_profiles = filter(lambda prof: name.lower() in prof.personalName.lower(), filtered_profiles)
            else:
                filtered_profiles = filter(lambda prof: name.lower() in (prof.lastName + prof.firstName).lower(), filtered_profiles)

        if tags:
            filtered_profiles = list(filter(lambda prof: prof.tags is not None and set(tags).issubset(prof.tags), filtered_profiles))

        result = [self.result_row_without_password_profile(profile) for profile in filtered_profiles]
        return Status.EMPTY.value if len(result) == 0 else json.dumps(result)
