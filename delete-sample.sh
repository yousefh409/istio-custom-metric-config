kubectl delete -f samples/sleep/sleep.yaml
kubectl delete -f samples/bookinfo/bookinfo.yaml
# kubectl delete -f samples/addons
cd istio-1.14.1
export PATH=$PWD/bin:$PATH
cd ..

istioctl manifest generate --set profile=demo | kubectl delete --ignore-not-found=true -f -
# istioctl tag remove default
#