from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app import db
from sqlalchemy.dialects.mysql import INTEGER


class MarksheetCBSE(db.Model):
    __tablename__ = 'marksheet_cbse'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    subject_code = db.Column(db.String(20), nullable=True)
    subject_name = db.Column(db.String(200), nullable=True)
    marks = db.Column(db.String(20), nullable=True)
    grade = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           )
    # children = relationship("user_categories")
