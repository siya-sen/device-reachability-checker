# Device Reachability Checker

A simple **Python tool** to monitor the reachability of network devices and servers using ICMP ping.

---

## Features

- ✅ Load devices from a **JSON configuration file**
- ✅ Check reachability using **ICMP ping**
- ✅ Retry mechanism for unreachable devices (2 retries)
- ✅ Log results with **timestamps**
- ✅ Configurable check interval (every 3 minutes)
- ✅ Windows compatible

---

## Technology Stack

- **Python 3.x**
- **subprocess** module for ping
- **json** for device configuration
- **datetime** for logging
- **time** module for intervals

---

## Setup & Usage

1. **Clone the repository**:

```bash

git clone https://github.com/YOUR_USERNAME/device-reachability-checker.git
cd device-reachability-checker
Ensure Python 3 is installed:

python --version
Run the script:

python reachability_checker.py
Configuration:

Edit devices.json to add/remove devices:

json

{
  "devices": [
    { "hostname": "Google DNS", "ip": "8.8.8.8" },
    { "hostname": "Router", "ip": "192.168.1.1" }
  ]
}
Logs:

All results are saved in reachability.log.

Example Output
Console:

Checking device reachability...

Google DNS (8.8.8.8) is Reachable [Attempt 1]
Local Server (192.168.1.100) is NOT Reachable after 3 attempts
Log file (reachability.log):

2025-05-13 15:10:01 - Google DNS (8.8.8.8) is Reachable [Attempt 1]
2025-05-13 15:10:10 - Local Server (192.168.1.100) is NOT Reachable after 3 attempts

Future Enhancements
Pull device list from a database instead of JSON
Send email/SMS alerts when a device is down
Add multi-threading for faster checks on large networks
Build a dashboard for visual reporting

Author
Siya Sen – BTech CSE 2023
GitHub

---

###  How to add this to GitHub

1. Create `README.md` in your project folder.
2. Copy–paste the content above.
3. Replace `YOUR_USERNAME` with your GitHub username.
4. Commit and push:

```bash
git add README.md
git commit -m "Add professional README"
git push
