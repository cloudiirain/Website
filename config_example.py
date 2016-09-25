import os
from RanobeHonyaku.utils import setup_file

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = setup_file["SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = "postgresql://localhost/ranobe_dev"