import requests

# Cisco Catalyst Center API details
BASE_URL = "https://sandboxdnac.cisco.com"

# Use your provided token directly
TOKEN = "PASTE_TOKEN_HERE"  # Replace with your actual token

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def get_topology():
    """Fetch network topology from Cisco Catalyst Center API."""
    # Correct endpoint for topology
    url = f"{BASE_URL}/PASTE_RESOURCE_URL_HERE"  # Replace with the correct URL
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        topology = response.json().get("response", {})

        nodes = topology.get("nodes", [])
        links = topology.get("links", [])

        print(f"✅ Topology fetched successfully!")
        print(f"📡 Total Nodes: {len(nodes)}")
        print(f"🔗 Total Links: {len(links)}\n")

        # Display a summary of nodes
        print("=== Nodes ===")
        for node in nodes:
            node_id = node.get("id", "N/A")
            label = node.get("label", "Unknown")
            device_type = node.get("deviceType", "Unknown")
            family = node.get("family", "Unknown")
            ip = node.get("ip", "Unknown")

            print(f"🧩 ID: {node_id}")
            print(f"🏷️  Label: {label}")
            print(f"🔧 Type: {device_type} | Family: {family}")
            print(f"🌐 IP: {ip}")
            print("-" * 50)

        # Display a summary of links
        print("\n=== Links ===")
        for link in links:
            source = link.get("source", "Unknown")
            target = link.get("target", "Unknown")
            link_status = link.get("linkStatus", "Unknown")
            print(f"🔗 {source} ➡️ {target} | Status: {link_status}")

    else:
        print(f"❌ Failed to retrieve topology: {response.status_code} - {response.text}")

# Run the function
get_topology()

