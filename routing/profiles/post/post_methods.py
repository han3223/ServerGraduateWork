from flask import Blueprint, request

from database.db import db
from database.dto.profile.insert.insert import DTOInsertProfile
from database.dto.profile.profile import DTOProfile

from database.models.profile import Profile

profile_post = Blueprint('profiles-post', __name__)

dto_profile = DTOInsertProfile(db)


@profile_post.route("/add", methods=['POST'])
def add_profile():
    json_data = request.data.decode('utf-8')
    model_profile = Profile.parse_raw(str(json_data))
    return dto_profile.add_profile(model_profile)
