import subprocess
import json
import sys

def get_pod_details(namespace, release_name):
    command = [
        "kubectl",
        "get",
        "pods",
        "-n",
        namespace,
        "-l",
        f"release={release_name}",
        "-o",
        "json"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        pods_data = json.loads(result.stdout)
        
        pod_details = []
        for pod in pods_data["items"]:
            details = {
                "name": pod["metadata"]["name"],
                "status": pod["status"]["phase"],
                "restarts": pod["status"]["containerStatuses"][0]["restartCount"] if pod["status"].get("containerStatuses") else 0,
                "ready": pod["status"].get("conditions", [{}])[0].get("status", "Unknown")
            }
            pod_details.append(details)
        
        return pod_details
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return []

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <namespace> <release_name>")
        print("Example: python script.py gk-test good-pod-release")
        sys.exit(1)
    
    namespace = sys.argv[1]
    release_name = sys.argv[2]
    
    print(f"Fetching pods for release '{release_name}' in namespace '{namespace}'...\n")
    
    pods = get_pod_details(namespace, release_name)
    
    if pods:
        print(f"Found {len(pods)} pod(s):\n")
        for pod in pods:
            print(f"Name: {pod['name']}")
            print(f"Status: {pod['status']}")
            print(f"Restarts: {pod['restarts']}")
            print(f"Ready: {pod['ready']}")
            print("-" * 50)
    else:
        print("No pods found or error occurred.")
        sys.exit(1)

if __name__ == "__main__":
    main()