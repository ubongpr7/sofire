#!/bin/bash

# Install pip3
echo "Installing pip3..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

# Upgrade pip3, setuptools, and wheel
echo "Upgrading pip3 and related tools..."
pip3 install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Django migrations
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
