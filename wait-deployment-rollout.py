import subprocess

def get_deployments():
    deployment_info = subprocess.run(["kubectl get deployment"], shell=True, capture_output=True, text=True).stdout.strip("\n").split("\n")
    # first row is column names
    deployment_info = deployment_info[1:]
    deployments = [x.split()[0] for x in deployment_info]
    return deployments

def rollout_status(deployment):
    print(f"Checking status of \"{deployment}\"")
    result = subprocess.run(f"kubectl rollout status deployment {deployment}", shell=True, capture_output=True, text=True).stdout
    print("\t", result)

if __name__ == "__main__":
    print("Getting deployments")
    deployments = get_deployments()
    print(f"\t Deployments: {deployments}")

    for deployment in deployments:
        rollout_status(deployment=deployment)