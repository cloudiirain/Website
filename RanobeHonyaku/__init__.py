from flask import Flask
from flask_migrate import Migrate

from RanobeHonyaku.database import db
from RanobeHonyaku.api.v1 import api_v1
from RanobeHonyaku.admin import admin

app = Flask("RanobeHonyaku")

# Load config files
app.config.from_object("config")

# Extension setup (e.g. database)
db.init_app(app)
Migrate(app, db)

# Registering the applications blueprints
app.register_blueprint(api_v1)
app.register_blueprint(admin)

# Error handlers and base application routes
# Technically a circular import, but this design pattern is recommended by flask docs (and works)
# http://flask.pocoo.org/docs/0.11/patterns/packages/
import RanobeHonyaku.views