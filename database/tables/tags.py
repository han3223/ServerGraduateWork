from sqlalchemy import Column, Integer, String

from database.db import db


class Tags(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(40))
    type = Column(String(30))
