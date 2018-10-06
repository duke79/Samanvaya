from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db
from app.data.tables.alchemy_base import db_type, DBType


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)
    # photo_url = db.Column(db.String(2013), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    # firebase_uid = db.Column(db.String(100), nullable=True)
    # admin = db.Column(db.Boolean, nullable=False, server_default=expression.false())
    if db_type == DBType.sqlite or db_type == DBType.mysql:
        marksheet_10 = db.Column(db.String, nullable=True)
        marksheet_12 = db.Column(db.String, nullable=True)
        marksheet_grad = db.Column(db.String, nullable=True)
        marksheet_post_grad = db.Column(db.String, nullable=True)
    if db_type == DBType.postgres:
        marksheet_10 = db.Column(JSONB, nullable=True)
        marksheet_12 = db.Column(JSONB, nullable=True)
        marksheet_grad = db.Column(JSONB, nullable=True)
        marksheet_post_grad = db.Column(JSONB, nullable=True)

    __table_args__ = (UniqueConstraint('name', 'phone_number', 'email', name='uix_1'),)

    # children = relationship("user_categories")
