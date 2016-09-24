from flask import request, jsonify
from flask_restful import Resource, abort

from app import db
# from models.series import Series

# shows or mutates a single series item
class Series(Resource):

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


# shows a list of all series, or POST to add new series
class SeriesList(Resource):

    def get(self):
        # mock data
        series = [
            {
                'id': 1,
                'title': u'Some title'
            },
            {
                'id': 2,
                'title': u'Another title'
            }
        ]

        return jsonify({'series': series})

    def post(self):
        # validation and sanitization
        if not request.json or not 'title' in request.json:
            abort(400)
        title = request.json['title']

        # commit to database
        #series = Series(title)
        # db.session.add(series)
        # db.session.commit()

        return jsonify({'series': 'yo'})

