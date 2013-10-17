# {{cookiecutter.verbose_project_name}}

{{cookiecutter.description}}

Project Setup
-------------

From the root project directory:

    $ mkvirtualenv {{cookiecutter.project_name}}
    $ pip install -r requirements.txt
    $ npm install -g grunt-cli
    $ npm install

At this point, you can fire up runserver. It will fire up Grunt as a child
process to watch JavaScript templates and Less styles, and set up a livereload
server to automatically refresh as you save files.

Config
------

The configuration relies somewhat on environment variables. Add the following
to your $VIRTUALENV/bin/postactivate:

    # Config Vars
    export DEBUG=True
    export DATABASE_URL=postgres://database_user:mypassword@localhost:5432/{{cookiecutter.project_name}}

This will use the user 'database_user' with 'mypassword' on the '{{cookiecutter.project_name}}' database.

Make sure to add the inverse to postdeactivate:

    # Unset config vars
    unset DEBUG
    unset DATABASE_URL

A better way to handle this will be forthcoming.
