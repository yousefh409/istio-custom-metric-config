# NOTE: RUN THESE COMMANDS YOURSELF, AS THERE IS A SLIGHT ISSUE WITH THE SCRIPT
# Starting minikube to store k8's cluster
    # Note: Need to update if using some other method
minikube start

# setup istioctl command
cd istio-1.14.1
export PATH=$PWD/bin:$PATH
cd ..

# setting up istio config
istioctl install -f istio-config.yaml -y # -d istio-1.14.1/manifests -y
kubectl label namespace default istio-injection=enabled

# Setting up sample k8's cluster
    # Note: Not needed if cluster already setup, or not using sample app
kubectl apply -f samples/bookinfo/bookinfo.yaml
kubectl apply -f samples/bookinfo/bookinfo-gateway.yaml

python3 apply-deployment-stats.py   

# minikube tunnel &

# set up dashboards (prometheus, jaeger, etc)
# kubectl apply -f istio-1.14.1/samples/addons

# Run `kubectl get deployments` and verify that all deployments are available