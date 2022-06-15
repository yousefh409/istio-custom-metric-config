minikube start

# setup istioctl command
cd istio-1.14.1
export PATH=$PWD/bin:$PATH
cd ..

istioctl install -f istio-config.yaml -d istio-1.14.1/manifests -y
kubectl label namespace default istio-injection=enabled

kubectl apply -f samples/bookinfo/bookinfo.yaml
kubectl apply -f samples/bookinfo/bookinfo.yaml

python3 apply-deployment-stats.py   