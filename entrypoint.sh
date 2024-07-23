#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Load initial data from fixtures
echo "Loading initial data from fixtures..."
python manage.py loaddata fixtures/*.json

# Start the server
echo "Starting server..."
python manage.py runserver  0.0.0.0:8000
exec "$@"
