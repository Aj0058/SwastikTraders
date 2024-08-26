#!/bin/bash

echo "BUILD START"

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
