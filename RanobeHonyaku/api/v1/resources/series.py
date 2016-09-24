from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from database import db_session
from models import Series
from api.v1.resources.chapter import chapter_list_fields

# fields to serialize when a single series is requested
series_detail_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "chapters": fields.List(fields.Nested(chapter_list_fields))
}

# fields to serialize when a list of series is requested
series_list_fields = {
    "id": fields.Integer,
    "title": fields.String,
}


# shows or mutates a single series item
class SeriesDetail(Resource):

    @marshal_with(series_detail_fields)
    def get(self, series_id):
        series = Series.query.get(series_id)
        if not series:
            abort(404)
        return series

    @marshal_with(series_detail_fields)
    def put(self, series_id):
        series = Series.query.get(series_id)
        if not series:
            abort(404)

        # validation, sanitization, and committing
        if not request.json or not 'title' in request.json:
            abort(400)
        series.title = request.json['title']
        db_session.commit()

        return series

    @marshal_with(series_detail_fields)
    def delete(self, series_id):
        series = Series.query.get(series_id)
        if not series:
            abort(404)

        # need to protect this against cascading deletes

        db_session.delete(series)
        db_session.commit()
        return series


# shows a list of all series, or POST to add new series
class SeriesList(Resource):

    @marshal_with(series_list_fields)
    def get(self):
        return Series.query.all()

    @marshal_with(series_detail_fields)
    def post(self):
        # validation and sanitization
        if not request.json or not 'title' in request.json:
            abort(400)
        title = request.json['title']

        # need to check if series already exists before adding

        # commit to database
        series = Series(title=title)
        db_session.add(series)
        db_session.commit()

        return series, 201

