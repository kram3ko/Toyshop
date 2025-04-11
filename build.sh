#!/usr/bin/env bash
# Exit on error

set -o errexit
# Installing uv
pip install --upgrave uv

# Installing dependencies from pyproject.toml
uv sync

# Collecting statics
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate
