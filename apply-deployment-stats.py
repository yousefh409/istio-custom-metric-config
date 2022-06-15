import os
import sys

os.system("kubectl  apply -f deployment.yaml")

def get_extra_stats(filename):
    pass

def get_services():
    pass

def get_updated_config(extra_stats):
    pass

def update_config(service, config):
    pass

if __name__ == "main":
    if len(sys.argv) == 0:
        extra_stats_file = "extraStats.txt"
        extra_stats = get_extra_stats(extra_stats_file)
    elif len(sys.argv) == 1:
        extra_stats_file = sys.argv[0]
        extra_stats = get_extra_stats(extra_stats_file)
    else:
        extra_stats = sys.argv[1:]

    services = get_services()
    updated_config = get_updated_config(extra_stats=extra_stats)

    for service in services:
        update_config(service=service, config=updated_config)

    


