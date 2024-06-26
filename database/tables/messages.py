from sqlalchemy import Column, Integer, Text, ForeignKey, Date, Time, Boolean
from sqlalchemy.orm import relationship

from database.db import db


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    message = db.Column(db.Text)
    messenger_id = db.Column(db.Integer, db.ForeignKey('messengers.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    # Определение отношений между таблицами
    messenger = db.relationship('Messengers', back_populates='messages')
    user = db.relationship('Profiles', back_populates='messages')
