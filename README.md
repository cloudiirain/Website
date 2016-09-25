# Website
The Ranobe-Honyaku website source code.

# Installation
* Make sure you have python3, setting up a virtualenv is strongly recommended
* Install postgresql. Create a db for this project and modify config.py URI for the database
* pip install -r requirements.txt
* Make sure you have a setup.json -- copy setup_example.json if you don't have one
* Make sure you have a config.py -- copy config_example.py if you don't have one
* If you have no migrations folder, run manage.py db init
* If databases models have changed run "manage.py db migrate"
* If your database file does not exist or migrations have not been applied, run "manage.py db upgrade"
* Run manage.py runserver to start server