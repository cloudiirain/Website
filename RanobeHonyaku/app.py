from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from views import home
from api import API
from epub import epub
from admin import admin
from utils import setup_file

# Create our flask instance and import config
app = Flask("RanobeHonyaku")
app.config.from_object("config")

# Registering database
db = SQLAlchemy(app)

# Registering the applications blueprints
app.register_blueprint(home)
app.register_blueprint(API)
app.register_blueprint(admin)
app.register_blueprint(epub)


# Our error handlers
@app.errorhandler(404)
def error_404_not_found(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(401)
def error_401_unauthorized(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(500)
def error_500_server_error(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(403)
def error_403_forbidden(e):
    return render_template("error.html", setup_file=setup_file, error=e)


# Run our dev server; Remove once app is in production setting!
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
