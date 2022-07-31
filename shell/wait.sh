#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
  
until ./shell/wait-for-it.sh "$host"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Running migrations"
python manage.py migrate

>&2 echo "Postgres is up - executing command"
exec "$@"
