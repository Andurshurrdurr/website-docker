import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'test.db'
SECRET_KEY = 'KEY_HERE'#
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
