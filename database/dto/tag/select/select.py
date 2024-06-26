from database.dto.tag.tag import DTOTag
from database.dto.values import Status
from database.tables.tags import Tags


class DTOSelectTag(DTOTag):

    def get_tags_by_type(self, type: str):
        tags = self.db.session.query(Tags).filter(Tags.type == type).all()
        result = [self.result_row_tag(tag) for tag in tags]
        return Status.EMPTY.value if len(result) == 0 else result
