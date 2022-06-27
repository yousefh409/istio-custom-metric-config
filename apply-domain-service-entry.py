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
        name: allpass-ext-http
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
        name: allpass-ext-https
        spec:
        hosts:
        - "*.{domain}"
        ports:
        - number: 443
            name: https
            protocol: HTTPS
        resolution: NONE
        location: MESH_EXTERNAL
    """

if __name__ == "__main__":
    # top_level_domains to track provided in file
    if len(sys.argv) == 1:
        top_level_domains_file = "top-level-domains.txt"
        top_level_domains = get_top_level_domains(top_level_domains_file)
    elif len(sys.argv) == 2:
        top_level_domains_file = sys.argv[1]
        top_level_domains = get_top_level_domains(top_level_domains_file)
    # top_level_domains to track provided as arguments
    else:
        top_level_domains = sys.argv[1:]

    
