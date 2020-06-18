release: python violance_analytics/manage.py makemigrations --noinput
release: python violance_analytics/manage.py migrate --noinput
web: sh -c 'cd ./violance_analytics/ && exec gunicorn violance_analytics.wsgi --log-file -'