from app import db
from app.data.tables import *


def initDB():
    # Dummy instantiation
    # category = Category()
    # channel = Channel()
    # user = User()

    # Initialize schema in mysql database
    db.create_all()


if __name__ == "__main__":
    initDB()
