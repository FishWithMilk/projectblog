web: gunicorn projectblog.wsgi
web: python projectblog/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT projectblog/settings.py