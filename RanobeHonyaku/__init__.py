from flask import Flask
from flask_migrate import Migrate

from RanobeHonyaku.database import db
from RanobeHonyaku.api.v1 import api_v1
from RanobeHonyaku.admin import admin

app = Flask("RanobeHonyaku")

# Load config files
app.config.from_object("config")
modules = {
    "migrate": None
}

# URI setup
'''
app.config["SQLALCHEMY_DATABASE_URI"] = \
        "postgresql://{}:{}@{}:{}/{}".format(app.config["DB_USERNAME"], app.config["DB_PASSWORD"],
                                             app.config["DB_HOSTNAME"], app.config["DB_PORT"],
                                             app.config["DB_DATABASE"])
'''

# Extension setup (e.g. database)
db.init_app(app)
modules["migrate"] = Migrate(app, db)

# Registering the applications blueprints
app.register_blueprint(api_v1)
app.register_blueprint(admin)

# Error handlers and base application routes
# Technically a circular import, but this design pattern is recommended by flask docs (and works)
# http://flask.pocoo.org/docs/0.11/patterns/packages/
import RanobeHonyaku.views