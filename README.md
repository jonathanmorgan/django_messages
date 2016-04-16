# django_messages

A simple re-usable Django application for storing messages from within django that should support both Python 2 and 3.  To start, just puts them in a database.  Eventually, might add ways to send them other places as well (email, message queue, etc.).

# Installation

Assumptions:

- You already have a django project, and your database is configured and tested.  If you don't, see the django tutorial for instructions on creating a django project.
- You are using a virtualenv, such that you don't have to run `pip` as root.  If not, add `sudo` in front of `pip` commands, or open a shell as root.

## Dependencies

- install python_utilites in your django project:

        cd <django_project_directory>
        git clone https://github.com/jonathanmorgan/python_utilities
        pip install -r ./python_utilities/requirements.txt
        
- install django_config and its requirements in your django project:

        cd <django_project_directory>
        git clone https://github.com/jonathanmorgan/django_config.git
        pip install -r ./django_config/requirements.txt
        
- install this project:

        cd <django_project_directory>
        git clone https://github.com/jonathanmorgan/django_messages.git
        pip install -r ./django_messages/requirements.txt

# Configuration

Update `settings.py` so that `taggit`, `django_config` and `django_messages` are in your `INSTALLED_APPS`.  Use the new-style apps.py syntax for `django_config` and `django_messages`.  The result should look like:

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'taggit',
        'django_config.apps.Django_ConfigConfig',
        'django_messages.apps.DjangoMessagesConfig',
    ]

# Database

In your django project folder, run the `migrate` command to create database table(s) for newly installed application(s):

    python manage.py migrate

# License

Copyright 2016-present (2016) Jonathan Morgan

This file is part of [https://github.com/jonathanmorgan/django_messages](https://github.com/jonathanmorgan/django_messages).

django_messages is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

django_messages is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with [https://github.com/jonathanmorgan/django_messages](https://github.com/jonathanmorgan/django_messages).  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).