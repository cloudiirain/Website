#!/usr/bin/env python3
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from RanobeHonyaku import app
from RanobeHonyaku.database import db
from RanobeHonyaku import models

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(host="127.0.0.1", port=5000, debug=True)

if __name__ == "__main__":
    manager.run()