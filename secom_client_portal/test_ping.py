import json
import time
import urllib.request

# The local URL pointing directly to your new Django API route
API_URL = "http://127.0.0.1:8000/api/device-ping/"

def send_hardware_ping(device_id, status, firmware, cpu, uptime):
    # Package up the authentic network telemetry payload
    payload = {
        "device_id": device_id,
        "status": status,
        "firmware_version": firmware,
        "telemetry": {
            "cpu_usage_percent": cpu,
            "uptime_hours": uptime
        }
    }
    
    # Convert the Python dictionary into raw JSON bytes
    json_bytes = json.dumps(payload).encode('utf-8')
    
    # Configure the HTTP headers
    req = urllib.request.Request(API_URL, data=json_bytes, method='POST')
    req.add_header('Content-Type', 'application/json')
    
    try:
        # Fire the packet across the local network to Django
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode('utf-8'))
            print(f"📡 [HTTP {response.status}] Success: {response_data['message']}")
    except urllib.error.HTTPError as e:
        error_message = e.read().decode('utf-8')
        print(f"❌ [HTTP {e.code}] Error: {error_message}")
    except Exception as e:
        print(f"❌ Network Error: {str(e)}")

# Run the Simulation 
if __name__ == "__main__":
    print("🚀 Starting Hardware Device Simulator...")
    
    # Target Device ID 1 (or whatever ID your device has in the admin panel)
    # simulate a healthy device checking in
    send_hardware_ping(
        device_id=1, 
        status="ONLINE", 
        firmware="v4.2.1", 
        cpu=14.5, 
        uptime=128
    )