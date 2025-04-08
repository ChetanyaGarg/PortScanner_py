```md
# Port Scanner

## Overview
A simple yet powerful **Python-based port scanner** for analyzing open ports on a given target IP address. This tool is useful for **security assessments**, ethical hacking, and learning about **network services**.

## Features
- Scan **multiple IP addresses** at once.
- Detect **open ports** using **TCP socket connections**.
- Adjustable **timeout settings** for improved accuracy.
- **Color-coded results** for better readability.
- **Fast and efficient**, with minimal resource consumption.

## Requirements
Ensure you have the following installed before running the script:
- Python 3.x
- `termcolor` library (for colored output)

Install dependencies using:
```bash
pip install termcolor
```

## Usage
Run the script in a terminal:
```bash
python3 port_scanner.py
```
Enter the target IP(s) and port range when prompted.

## Example Output
```
[*] Enter The Targets To Scan (separate multiple IPs with ","): scanme.nmap.org
[*] Enter Till Which Port Do You Want To Scan: 100
[*] Scanning Multiple Targets ->
[-] Port Closed 21
[+] Port Open 80
[-] Port Closed 443
```

## Legal Disclaimer
This tool is intended **only for ethical purposes**. **Do not** use this tool for unauthorized scanning or penetration testing without explicit permission.

## License
MIT License – Free to use, modify, and distribute.
```

---
