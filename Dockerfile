FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .  .

#SET the multiprocess directory environment variable
ENV PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus_metrics   

RUN mkdir -p /tmp/prometheus_metrics

#start gunicorn with four workers 
CMD ["gunicorn","foodapp.wsgi:application","--bind","0.0.0.0:8000","--workers","4","-c","gunicorn.conf.py"]