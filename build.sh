#!/bin/bash

# Install pip
echo "Installing pip..."
python3.9 -m ensurepip --upgrade || true
python3.9 -m pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

# Django migrations
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
