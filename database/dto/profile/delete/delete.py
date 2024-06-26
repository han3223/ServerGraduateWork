from database.dto.profile.profile import DTOProfile
from database.models.profile import Profile


class DTODeleteProfile(DTOProfile):
    def delete_profile(self, profile_id):
        profile = self.db.session.query(Profile).filter_by(id=profile_id).first()
        self.db.session.delete(profile)
        self.db.session.commit()