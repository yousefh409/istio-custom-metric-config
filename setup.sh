# Starting minikube to store k8's cluster
    # Note: Need to update if using some other method
# minikube start --cpus 4 --memory 8192

# setup istioctl command
cd istio-1.14.1
export PATH=$PWD/bin:$PATH
cd ..

# setting up istio config
istioctl install -f istio-config.yaml -y # -d istio-1.14.1/manifests -y
kubectl label namespace default istio-injection=enabled
# wait for all deployments to be rolled out
python3 wait-deployment-rollout.py
# upload the extra stats configuration to each deployment
python3 apply-deployment-stats.py   
# check that all services have been rolled out
# python3 wait-deployment-rollout.py

# IMPORTANT: Run `minikube tunnel` after running this script to expose the app if using minikube