#!/bin/bash
# build the project
echo "Building the project"
python3.9 -m pip3 install -r requirements.txt

echo "Makemigrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collecting staticfiles"
python3.9 manage.py collectstatic --noinput --clear
