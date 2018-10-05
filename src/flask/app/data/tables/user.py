from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)
    photo_url = db.Column(db.String(2013), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    firebase_uid = db.Column(db.String(100), nullable=True)
    admin = db.Column(db.Boolean, nullable=False, server_default=expression.false())
    # children = relationship("user_categories")
