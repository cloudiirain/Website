#!usr/bin/python

from app import db
from models import user, series, chapter

db.create_all()