# web_attack_gui

A **Python-based GUI tool** to perform network and web security scans, integrating multiple modules for penetration testing and reconnaissance.

---

## Features

- **Ping Module:** Check host availability and latency  
- **Nmap Module:** Scan network hosts and services  
- **Whois Module:** Retrieve domain registration information  
- **HTTP Headers Module:** Fetch HTTP headers from a URL  
- **DNS Lookup Module:** Query A, MX, NS, TXT records  
- **Port Scanner Module:** Scan ports and detect open services  
- **Subdomain Enumeration Module:** Discover subdomains of a target domain  
- **Reverse IP Lookup Module:** Find other domains hosted on the same server IP  
- **Vulnerability Scan Module:** Basic CVE lookup for scanned services  
- **Save Results:** Export scan results to files  

---

## Setup & Installation

1. Clone/download the repository:

```bash
git clone https://github.com/<yourusername>/web_attack_gui.git
cd web_attack_gui

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 main.py

web_attack_gui/
├── main.py
├── requirements.txt
├── README.md
├── assets/
│   ├── ping.png
│   ├── nmap.png
│   ├── whois.png
│   ├── http.png
│   ├── dns.png
│   ├── port.png
│   ├── subdomain.png
│   ├── reverse_ip.png
│   └── vuln.png
├── modules/
│   ├── ping_module.py
│   ├── nmap_module.py
│   ├── whois_module.py
│   ├── http_headers_module.py
│   ├── dns_lookup_module.py
│   ├── port_scanner_module.py
│   ├── subdomain_module.py
│   ├── reverse_ip_module.py
│   ├── vuln_scan_module.py
│   └── save_results_module.py
├── outputs/
│   └── [saved scan results]
└── tests/
    └── [test scripts]

Usage

Open the GUI (main.py)

Select a module tab (Ping, Nmap, Whois, HTTP Headers, DNS Lookup, Port Scanner, Subdomain, Reverse IP, Vulnerability Scan)

Enter the target (domain, IP, or service) in the input box

Click Run to start the scan

View results in the output box

Click Save Results to export results

Technologies Used:
Python 3
PyQt5 (GUI Framework)
Requests
dnspython
aiohttp
