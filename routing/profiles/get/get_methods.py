import random

from flask import request, Blueprint

from database.db import db
from database.dto.profile.select.select import DTOSelectProfile
from email_factory.email_factory import EmailFactory

profile_get = Blueprint('profiles-get', __name__)

dto_profile = DTOSelectProfile(db)


@profile_get.route("/check-by-email", methods=['GET'])
def get_profile_by_email():
    email = request.args.get('email')
    return dto_profile.select_profile_by_email(email)


@profile_get.route("/check-by-phone-number", methods=['GET'])
def get_profile_by_phone_number():
    phone_number = request.args.get('phoneNumber')
    return dto_profile.select_profile_by_phone_number(phone_number)


@profile_get.route("/get-by-email-and-password", methods=['GET'])
def get_profile_by_email_and_password():
    email = request.args.get('email')
    password = request.args.get('password')
    return dto_profile.select_profile_by_email_and_password(email, password)


@profile_get.route("/get-by-personal-name", methods=['GET'])
def get_profile_by_personal_name():
    personal_name = request.args.get('personalName')

    return dto_profile.select_profile_by_personal_name(personal_name)


@profile_get.route("/get-all-without-password", methods=['GET'])
def get_all_profile_without_password():
    return dto_profile.select_all_profiles_without_password()


@profile_get.route("/get-without-password-by-id", methods=['GET'])
def get_profile_by_id_without_password():
    id_profile = request.args.get('id')

    return dto_profile.get_profile_by_id_without_password(int(id_profile))


@profile_get.route("/get-recovery-code-by-last-name-and-phone-number", methods=['GET'])
def get_recovery_code_using_last_name_and_phone_number():
    last_name = request.args.get('lastName')
    phone_number = request.args.get('phoneNumber')

    return dto_profile.get_recovery_code_using_last_name_and_phone_number(last_name, phone_number)


@profile_get.route("/get-recovery-code-by-last-name-and-email", methods=['GET'])
def get_recovery_code_using_last_name_and_email():
    last_name = request.args.get('lastName')
    phone_number = request.args.get('email')

    return dto_profile.get_recovery_code_using_last_name_and_email(last_name, phone_number)


@profile_get.route("/get-verification-code", methods=['GET'])
def get_verify_code():
    email = request.args.get('email')

    code = random.randint(1000, 9999)

    print(code)

    gmailSender = EmailFactory()
    template_variables = {'code': code}
    gmailSender.send_email(email, **template_variables)

    return str(code)


@profile_get.route("/get-personal-name-name-tags", methods=['GET'])
def get_name_personal_name_tags():
    name = request.args.get('name')
    tags = request.args.get('tags')

    return dto_profile.get_profiles_by_name_personal_name_tags(name, tags)
