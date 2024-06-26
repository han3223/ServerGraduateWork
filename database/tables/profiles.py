from sqlalchemy.orm import relationship

from database.db import db
from sqlalchemy import Column, Integer, String, LargeBinary, Text

from database.tables.messengers import Messengers


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lastName = db.Column(db.String(100))
    firstName = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))
    phoneNumber = db.Column(db.String(20))
    email = db.Column(db.String(100))
    password = db.Column(db.String(150))
    image = db.Column(db.LargeBinary, nullable=True)
    tags = db.Column(db.Text, nullable=True)
    personalName = db.Column(db.String(30), nullable=True)
    personalInfo = db.Column(db.String(120), nullable=True)
    friends = db.Column(db.Text, nullable=True)

    document = db.relationship('Documents', back_populates='user')
    messages = db.relationship('Messages', back_populates='user')
