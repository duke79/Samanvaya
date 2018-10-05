import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db
from sqlalchemy.dialects.mysql import INTEGER


class MarksheetCBSE(db.Model):
    __tablename__ = 'marksheet_cbse'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    roll_number = db.Column(db.String(200), nullable=True)
    name_candidate = db.Column(db.String(200), nullable=True)
    name_father = db.Column(db.String(200), nullable=True)
    name_mother = db.Column(db.String(200), nullable=True)
    d_o_b = db.Column(db.Date, nullable=False)
