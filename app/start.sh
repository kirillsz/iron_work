#!/bin/bash

pip freeze > requirements.txt

python manage.py makemigrations && python manage.py migrate

gunicorn iron_work.wsgi:application -b 0.0.0.0:8000 -w 3 --reload