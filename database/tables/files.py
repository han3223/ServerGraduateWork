from sqlalchemy import Column, Integer, LargeBinary
from sqlalchemy.orm import relationship

from database.db import db


class Files(db.Model):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file = Column(LargeBinary)

    document = relationship('Documents', back_populates='file')
