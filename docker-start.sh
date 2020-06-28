# Apply database migrations
echo "Apply database migrations" > /dev/console
python manage.py migrate

echo "Collect static files" > /dev/console
rm -rf staticfiles
python manage.py collectstatic
cp -R staticfiles/* static

# Start server
echo "Starting server"
gunicorn summer_camp_api_project.wsgi:application --bind 0.0.0.0:8000
