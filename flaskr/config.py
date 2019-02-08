import os
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.db'
SECRET_KEY = os.environ["SECRET_KEY"]