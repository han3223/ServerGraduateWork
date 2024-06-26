from flask import Blueprint, request

from database.db import db
from database.dto.profile.update.update import DTOUpdateProfile
from routing.profiles.get.get_methods import profile_get

profile_put = Blueprint('profiles-put', __name__)

dto_profile = DTOUpdateProfile(db)


@profile_put.route("/update-personal-name", methods=['PUT'])
def update_personal_name():
    email = request.args.get('email')
    personal_name = request.args.get('personalName')

    return dto_profile.update_personal_name(email, personal_name)


@profile_put.route("/update-personal-info", methods=['PUT'])
def update_personal_info():
    email = request.args.get('email')
    personal_info = request.args.get('personalInfo')

    return dto_profile.update_personal_info(email, personal_info)


@profile_put.route("/update-phone-number", methods=['PUT'])
def update_number_phone():
    email = request.args.get('email')
    phone_number = request.args.get('phoneNumber')

    return dto_profile.update_number_phone(email, phone_number)


@profile_put.route("/update-email", methods=['PUT'])
def update_email():
    old_email = request.args.get('oldEmail')
    new_email = request.args.get('newEmail')

    return dto_profile.update_email(old_email, new_email)


@profile_put.route("/update-password", methods=['PUT'])
def update_password():
    email = request.args.get('email')
    old_password = request.args.get('oldPassword')
    new_password = request.args.get('newPassword')

    return dto_profile.update_password(email, old_password, new_password)


@profile_put.route("/update-tags", methods=['PUT'])
def update_tag():
    email = request.args.get('email')
    tags = request.args.get('tags')

    return dto_profile.update_tags(email, tags)


@profile_put.route("/update-password-by-phone-number", methods=['PUT'])
def update_password_using_phone_number():
    phone_number = request.args.get('phoneNumber')
    new_password = request.args.get('newPassword')

    return dto_profile.update_password_using_phone_number(phone_number, new_password)


@profile_put.route("/update-password-by-email", methods=['PUT'])
def update_password_using_email():
    email = request.args.get('email')
    new_password = request.args.get('newPassword')

    return dto_profile.update_password_using_email(email, new_password)
