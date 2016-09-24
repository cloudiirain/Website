from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from database import db_session
from models import Chapter

# fields to serialize when a single chapter is requested
chapter_detail_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String
}

# fields to serialize when a list of chapters is requested
chapter_list_fields = {
    "id": fields.Integer,
    "title": fields.String,
}