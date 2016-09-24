# Website #
The Ranobe-Honyaku website source code.

## Installation ##

### Prerequisites ###
* python3
* virtualenv
* Flask
* PostgreSQL

### Database Setup ###
~~~~
> psql
=# DELETE DATABASE ranobe_dev;
=# CREATE DATABASE ranobe_dev;
=# \q
~~~~

### Clone and set up virtualenv ###
~~~~
git clone https://github.com/Ranobe-Honyaku/Website.git
cd Website
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
cp setup_example.json setup.json
~~~~
At this point, open setup.json. You will probably need to change `SQLALCHEMY_DATABASE_URI` to
the path of your local database, provide login credentials, etc. Try this string format:
~~~~
"postgresql://username:password@host:port/database"
"postgresql://scott:tiger@localhost:5432/ranobe_dev"
or
"postgresql://localhost/ranobe_dev" <-- note: I did get this to work too on my machine
~~~~

### Run migrations on your local database and startapp ###
~~~~
(optional) python manage.py db init
(optional) python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
~~~~
If you are git cloning from master, you most likely won't need to run init or migrate. `init` should
only be run if you are missing the `migrations/` directory. `migrate` should be run whenever you
modify the model to prepare migrations.

`upgrade` is run to apply new migrations to your database, and generally should always been run when
cloning or pulling from master. If you having migration/database issues after cloning/pulling, you
may want to consider dropping your database and recreating it.