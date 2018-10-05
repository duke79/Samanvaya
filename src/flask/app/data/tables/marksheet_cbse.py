import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db


class MarksheetCBSE(db.Model):
    __tablename__ = 'marksheet_cbse'
    roll_number = db.Column(db.String(200), nullable=True)
    name_candidate = db.Column(db.String(200), nullable=True)
    name_father = db.Column(db.String(200), nullable=True)
    name_mother = db.Column(db.String(200), nullable=True)
    d_o_b = db.Column(db.Date, nullable=False)
