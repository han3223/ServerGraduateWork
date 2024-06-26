from sqlalchemy import Column, Integer, String, LargeBinary, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from database.db import db


class Documents(db.Model):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    category = Column(String(50))
    file_id = Column(Integer, ForeignKey('files.id', ondelete='CASCADE'))
    date = Column(Date)
    image = Column(LargeBinary, nullable=True)
    user_id = Column(Integer, ForeignKey('profiles.id'))
    tags = Column(Text)
    description = Column(Text, nullable=True)

    # Определение отношений между таблицами
    user = relationship('Profiles', back_populates='document', uselist=False)
    file = relationship('Files', back_populates='document', uselist=False)
