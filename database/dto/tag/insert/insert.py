from psycopg2 import IntegrityError

from database.dto.profile.profile import DTOProfile
from database.models.tag import Tag
from database.tables.tags import Tags


class DTOInsertTag(DTOProfile):
    def add_tag(self, model_tag: Tag):
        new_tag = Tags(title=model_tag.title, type=model_tag.type)
        self.db.session.add(new_tag)

        try:
            self.db.session.commit()
            return new_tag.id
        except IntegrityError:
            self.db.session.rollback()
            return IntegrityError.diag
