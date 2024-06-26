import json
from psycopg2 import IntegrityError

from database.dto.profile.profile import DTOProfile
from database.models.profile import Profile
from database.tables.profiles import Profiles
from hash.hash_password import HashPassword


class DTOInsertProfile(DTOProfile):
    def add_profile(self, profile: Profile):
        hashed_password = HashPassword.hash_password(profile.password.replace(" ", "+"))

        new_profile = Profiles(
            lastName=profile.lastName,
            firstName=profile.firstName,
            patronymic=profile.patronymic,
            phoneNumber=profile.phoneNumber,
            email=profile.email,
            password=hashed_password,
            image=profile.image,
            tags=",".join(map(str, profile.tags)) if profile.tags else None,
            personalName=profile.personalName,
            personalInfo=profile.personalInfo,
            friends=",".join(map(str, profile.friends)) if profile.friends else None
        )

        self.db.session.add(new_profile)
        try:
            self.db.session.commit()
            return json.dumps(self.result_row_profile(new_profile))
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag
