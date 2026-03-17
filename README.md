Features:
1. Containarizing the app and exposing on 8000 port 
    - here used gunicorn to maintain multiple workers to serve concurrent requests
2. Adding metrics exporter (exporter.py) and exposing on 8001 port
3. Added PrometheusBeforeMiddleware and PrometheusAfterMiddleware in settings.py to calculate exact time taken by the request to complete.
4. Build/ pull the docker image 'pknashi/food-app:1.0' and using deploy yaml run the containers.