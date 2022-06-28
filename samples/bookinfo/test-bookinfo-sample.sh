# Make sure to run `minikube tunnel`` before this

export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')

export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
echo "$GATEWAY_URL"

export SOURCE_POD=$(kubectl get pod -l app=sleep -o jsonpath='{.items..metadata.name}' | head -n1 | cut -d " " -f1)
kubectl exec "$SOURCE_POD" -c sleep -- curl "http://$GATEWAY_URL/productpage"
#  curl "http://$GATEWAY_URL/productpage"
# for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done


kubectl exec "$(kubectl get pod -l app=productpage -o jsonpath='{.items[0].metadata.name}')" -c istio-proxy -- curl -sS 'localhost:15000/stats/prometheus' | grep istio_requests_total
