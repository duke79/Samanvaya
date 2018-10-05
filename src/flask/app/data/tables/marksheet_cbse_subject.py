import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db
from sqlalchemy.dialects.mysql import INTEGER


class MarksheetCBSESubject(db.Model):
    __tablename__ = 'marksheet_cbse_subject'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    subject_code = db.Column(db.String(20), nullable=True)
    subject_name = db.Column(db.String(200), nullable=True)
    marks = db.Column(db.String(20), nullable=True)
    grade = db.Column(db.String(20), nullable=True)
