release: python violance_analytics/manage.py migrate
web: sh -c 'cd ./violance_analytics/ && exec gunicorn violance_analytics.wsgi --log-file -'