import subprocess
import sys
from xml import dom

def get_top_level_domains(filename):
    with open(filename) as f:
        top_level_domains = f.readlines()
    # strip newline
    top_level_domains = [x.strip("\n") for x in top_level_domains]
    return top_level_domains

def get_service_entry(domain):
    return f"""
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: {domain}-pass-ext-http
spec:
  hosts:
  - "*.{domain}"
  ports:
  - number: 80
    name: http
    protocol: HTTP
  resolution: NONE
  location: MESH_EXTERNAL
---
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: {domain}-pass-ext-https
spec:
  hosts:
  - "*.{domain}"
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  resolution: NONE
  location: MESH_EXTERNAL"""

def apply_service_entry(service_entry):
    result = subprocess.run(f"kubectl apply -f - <<EOF\n" + service_entry + "\nEOF", shell=True, capture_output=True, text=True)
    print(result.stdout, result.stderr)

if __name__ == "__main__":
    # top_level_domains to track provided in file
    if len(sys.argv) == 1:
        top_level_domains_file = "domain-suffixes.txt"
        top_level_domains = get_top_level_domains(top_level_domains_file)
    elif len(sys.argv) == 2:
        top_level_domains_file = sys.argv[1]
        top_level_domains = get_top_level_domains(top_level_domains_file)
    # top_level_domains to track provided as arguments
    else:
        top_level_domains = sys.argv[1:]

    for domain in top_level_domains:
        print(f"Applying Service Entry for {domain}")
        service_entry = get_service_entry(domain=domain)
        apply_service_entry(service_entry=service_entry)
    
    
