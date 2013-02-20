Haproxy manager
===============

Haproxy manager is a simple daemon that generates haproxy configuration files
through a simple HTTP interface.


HTTP Interface
--------------

Haproxy manager follows the REST HTTP interface and provides some simple URL to
manage haproxy configuration files.

Supported URLs:

Get the list of configuration files

        GET /list

Get the list of frontend configuration files

        GET /list/frontend

Get all informations for a given type and file name

        GET /type/frontend/name/machine0001

Create or update the data for a given type and file name

        PUT /type/frontend/name/machine0001
        {"maxconn": 30000}

Delete the file for the frontend configuration of machine0001

        DELETE /type/frontend/name/machine0001


Development
-----------

Almost everything you need will be available via `dev.makefile`.

To bootstrap your environment just run:

        make -f dev.makefile bootstrap

All the dependencies will be installed using virtualenv on .venv directory.

Just read the `dev.makefile` file for more informations on how to run the commands.


License
-------

APACHE 2.0
