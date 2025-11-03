# ---------------------------------------------
# Cisco DNAC API Reference Guide:
# https://developer.cisco.com/docs/dna-center/2-3-5/cisco-dna-center-2-3-5-api-overview/
# ---------------------------------------------


import requests

# Cisco DNA Center API details
BASE_URL = "https://sandboxdnac.cisco.com"

# Use your provided token directly
TOKEN = "PASTE_TOKEN_HERE"  # Replace with your actual token

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def get_devices():
    """Fetch network devices from Cisco DNA Center API."""
    url = f"{BASE_URL}/PASTE_ENDPOINT_URL_HERE"  # Replace with the correct endpoint
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        devices = response.json().get("response", [])

        if not devices:
            print("❌ No devices found.")
            return

        for device in devices:
            # Ensure we handle missing fields safely
            device_id = device.get("id", "N/A")
            hostname = device.get("hostname", "Unknown")
            ip_address = device.get("managementIpAddress", "Unknown")

            # Extract device type (alternative fields used if "type" is missing)
            device_type = device.get("type") or device.get("family") or device.get("platformId") or "Unknown"

            print(f"📌 Device ID: {device_id}")
            print(f"🔹 Hostname: {hostname}")
            print(f"🌐 IP Address: {ip_address}")
            print(f"🔧 Device Type: {device_type}")  # Correctly fetches the type
            print("-" * 50)  # Separator for readability

    else:
        print(f"❌ Failed to retrieve devices: {response.status_code} - {response.text}")

# Run the function
get_devices()

