class DTOProfile:
    def __init__(self, db):
        self.db = db

    def result_row_profile(self, row):
        return {
            "id": row.id,
            "lastName": row.lastName,
            "firstName": row.firstName,
            "patronymic": row.patronymic,
            "phoneNumber": row.phoneNumber,
            "email": row.email,
            "password": row.password,
            "image": row.image,
            "tags": row.tags,
            "personalName": row.personalName,
            "personalInfo": row.personalInfo,
            "friends": row.friends.split(",") if row.friends else [],
        }

    def result_row_without_password_profile(self, row):
        return {
            "id": row.id,
            "lastName": row.lastName,
            "firstName": row.firstName,
            "patronymic": row.patronymic,
            "phoneNumber": row.phoneNumber,
            "email": row.email,
            "image": row.image,
            "tags": row.tags,
            "personalName": row.personalName,
            "personalInfo": row.personalInfo,
            "friends": row.friends.split(",") if row.friends else [],
        }

