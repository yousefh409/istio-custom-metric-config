import subprocess
import sys

def get_extra_stats(filename):
    with open(filename) as f:
        extra_stats = f.readlines()
    # strip newline
    extra_stats = [x.strip("\n") for x in extra_stats]
    return extra_stats

def get_deployments():
    deployment_info = subprocess.run(["kubectl get deployment"], shell=True, capture_output=True, text=True).stdout.strip("\n").split("\n")
    # first row is column names
    deployment_info = deployment_info[1:]
    deployments = [x.split()[0] for x in deployment_info]
    return deployments


def get_updated_config(extra_stats):
    joined_stats = ",".join(extra_stats)
    return f'{{"spec":{{"template":{{"metadata":{{"annotations":{{"sidecar.istio.io/extraStatTags": "{joined_stats}"}}}}}}}}}}'

def update_config(deployment, config):
    subprocess.run(f"kubectl patch deployment {deployment} -p '{config}'", shell=True)

if __name__ == "__main__":
    # stats to track provided in file
    if len(sys.argv) == 1:
        extra_stats_file = "extraStats.txt"
        extra_stats = get_extra_stats(extra_stats_file)
    elif len(sys.argv) == 2:
        extra_stats_file = sys.argv[1]
        extra_stats = get_extra_stats(extra_stats_file)
    # stats to track provided as arguments
    else:
        extra_stats = sys.argv[1:]

    print("Getting deployments")
    deployments = get_deployments()
    print(f"\t Deployments: {deployments}")
    updated_config = get_updated_config(extra_stats=extra_stats)

    print("Updating configurations")
    for deployment in deployments:
        update_config(deployment=deployment, config=updated_config)
    print("Configurations upgraded \n\tPlease give the changes a minute or two to propogate")
