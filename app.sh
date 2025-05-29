alembic upgrade head

cd meteo_wt && gunicorn meteo_wt.wsgi:application  --bind 0.0.0.0:80
