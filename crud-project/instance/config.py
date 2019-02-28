import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_crud.sqlite')
SECRET_KEY = 'my-secret-key-0001010'
