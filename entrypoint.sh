#!/bin/sh

echo "Waiting for postgres..."

while [ "$(pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT)" != "$POSTGRES_HOST:$POSTGRES_PORT - accepting connections" ]; do
  sleep 1
done

echo "PostgreSQL started"

if [ "$SERVICE_NAME" = "app" ]; then

  echo " --- --- --- --- --- --- --- --- --- "
  echo "Applying database migrations"
  python manage.py migrate --noinput

  if [ "$INITIAL_SETUP" = true ]; then

    echo " --- --- --- --- --- --- --- --- --- "
    echo "Creating default superuser"
    python manage.py createsuperuser --username="$DJANGO_SUPER_USERNAME" --email="$DJANGO_SUPER_USER_EMAIL" --no-input

  fi

#  echo " --- --- --- --- --- --- --- --- --- "
#  echo "Compiling translations"
#  django-admin compilemessages --ignore=env

fi

echo " --- --- --- --- --- --- --- --- --- "
echo "Starting server"
exec "$@"
