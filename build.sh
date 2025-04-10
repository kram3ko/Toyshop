#!/usr/bin/env bash
# Exit on error

set -o errexit
# Installing uv
pip install -r requirements.txt

# Installing dependencies from requirements.txt або pyproject.toml
# Apply any outstanding database migrations

python manage.py migrate
