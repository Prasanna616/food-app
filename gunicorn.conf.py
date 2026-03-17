import os
from prometheus_client import multiprocess

#This runs when worker process exits
def child_exit(server,worker):
    multiprocess.mark_process_dead(worker.pid)