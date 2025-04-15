#! /bin/bash

echo 'starting deployment'

#project source directory
cd /home/pkweb/food-app

git pull origin newfeature

python manage.py collectstatic --noinput

#reload the webapp
touch /var/www/pkweb_pythonanywhere_com_wsgi.py

echo 'Deployment completed successfully'