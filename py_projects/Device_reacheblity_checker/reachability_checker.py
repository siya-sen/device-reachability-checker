import json
import subprocess
import time
from datetime import datetime

# Load devices from config file
def load_devices():
    with open("devices.json", "r") as file:
        return json.load(file)["devices"]

# Ping a device using Windows-style command
def ping_device(ip):
    try:
        result = subprocess.run(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL)
        return result.returncode == 0
    except:
        return False

# Check if device is reachable with retries
def check_device(device):
    name = device["hostname"]
    ip = device["ip"]
    for attempt in range(3):  # First try + 2 retries
        if ping_device(ip):
            status = f" {name} ({ip}) is Reachable [Attempt {attempt+1}]"
            print(status)
            log(status)
            return
        time.sleep(1)
    status = f" {name} ({ip}) is NOT Reachable after 3 attempts"
    print(status)
    log(status)

# Log result to file with timestamp
def log(message):
    with open("reachability.log", "a") as logfile:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"{timestamp} - {message}\n")

# Main function to check all devices every 3 minutes
def main():
    while True:
        print("\n Checking device reachability...\n")
        devices = load_devices()
        for device in devices:
            check_device(device)
        print(" Waiting for 3 minutes before next check...\n")
        time.sleep(180)

if __name__ == "__main__":
    main()
