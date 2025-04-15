#! /bin/bash

echo 'starting deployment'

git pull origin newfeature

python manage.py collectstatic --noinput

#reload the webapp
touch /var/www/pkweb_pythonanywhere_com_wsgi.py

echo 'Deployment completed successfully'