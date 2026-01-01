#! /bin/bash

echo 'starting deployment'

#project source directory
cd /home/pkweb/food-app/

echo 'start git pull'
git fetch origin
git reset --hard origin/newfeature
git pull origin newfeature

pip install -r requirement.txt

python manage.py collectstatic --noinput

#reload the webapp
touch /var/www/pkweb_pythonanywhere_com_wsgi.py

echo 'Deployment completed successfully'