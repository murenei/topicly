=======================================================
Topicly
=======================================================

A webapp that uses natural language processing to analyse newspaper article sentiment and topics.

Stack \n
Postgres \n
Django \n
JS \n
Bootstrap \n

Initial setup:
`virtualenv topicly-env -p 3.6`

`cd topicly-env`

`git clone...`

`cd topicly`

`pip install -r requirements`

`export DJANGO_SETTINGS_MODULE=settings.dev`

`python manage.py migrate`

`pthon manage.py loaddata '<filename>'`

`python manage.py createsuperuser`

`python manage.py runserver 7777`

That should have you setup.
