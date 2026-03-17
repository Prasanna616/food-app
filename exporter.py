import os 
from wsgiref.simple_server import make_server
from prometheus_client import  CollectorRegistry,multiprocess, make_wsgi_app

def make_metrics_app():
    """
     This function creates a WSGI app that automatically 
     collects metrics from all Gunicorn workers in the shared folder.
    """
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return make_wsgi_app(registry)
        

if __name__=='__main__':
    #Ensure the environment variable is set 
    if not os.environ.get('PROMETHEUS_MULTIPROC_DIR'):
        print("WARNING: PROMETHEUS_MULTIPROC_DIR is not set!")

    #create the app and start the server
    app = make_metrics_app()

    httpd = make_server('0.0.0.0',8001,app)
    print("Side car listening on port 8001")
    httpd.serve_forever()