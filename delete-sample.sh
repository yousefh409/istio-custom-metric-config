kubectl delete -f samples/sleep/sleep.yaml
kubectl delete -f samples/bookinfo/bookinfo.yaml
kubectl delete -f samples/addons
# istioctl manifest generate --set profile=demo | kubectl delete --ignore-not-found=true -f -
# istioctl tag remove default
