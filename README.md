**About**
* This Github Repo contains configurations and code that allows one to easily customize metrics in an istio cluster

Make sure to give permissions to of the scripts you make use of:
* `chmod +x {file}`

**Setting up Istio on Cluster**
1. Clone the git repository at https://github.infra.cloudera.com/yousefh/istio-cluster-config
2. Download istio using ``curl -L https://istio.io/downloadIstio | sh -``
3. Run the ./setup.sh script to setup istio and apply the necessary updates to your deployments
4. Run ``minikube tunnel`` if using minikube
5. You’re all set! If running the bookinfo sample app and want to test, run the ./test-bookinfo-sample.sh script

**Viewing Grafana Dashboard**
1. Make sure Istio is all setup, following the steps from the previous part
2. Run the ./setup-dashboards.sh script
3. Run ``istioctl dashboard grafana`` to start the grafana dashboard
4. Import your chosen Grafana dashboard from the grafana-dashboards folder of the repository
5.View/Create all the graphs you can think of!
