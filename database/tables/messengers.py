from sqlalchemy import Column, Integer, ForeignKey, Text, ARRAY
from sqlalchemy.orm import relationship

from database.db import db


class Messengers(db.Model):
    __tablename__ = 'messengers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    participants = Column(Text)

    # Определение отношений между таблицами
    messages = relationship('Messages', back_populates='messenger')
