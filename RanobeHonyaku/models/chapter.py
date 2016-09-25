from RanobeHonyaku.database import db

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    body = db.Column(db.String(1000000))

    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))

    def __init__(self, title, body, series):
        self.title = title
        self.body = body
        self.series = series

    def __repr__(self):
        return '<Chapter %r>' % (self.series.title + ": " + self.title)