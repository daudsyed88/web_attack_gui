# Local mock CVE database for testing GUI
MOCK_CVE_DB = {
    "Apache 2.4.52": [
        "CVE-2021-41773: Path traversal vulnerability in Apache 2.4.52",
        "CVE-2021-42013: Remote code execution in Apache 2.4.52"
    ],
    "nginx 1.20.1": [
        "CVE-2021-23017: Nginx 1.20.1 buffer overflow vulnerability"
    ],
    "OpenSSH 8.2p1": [
        "CVE-2020-14145: OpenSSH 8.2p1 user enumeration issue"
    ],
    "Microsoft-IIS 10.0": [
        "CVE-2020-0674: Remote code execution in IIS 10.0"
    ]
}

def run_vuln_scan(service_banner):
    """
    Checks the service banner against a local mock CVE database.
    Returns matching CVEs or a friendly message if none found.
    """
    results = MOCK_CVE_DB.get(service_banner)
    if results:
        return "\n".join(results)
    else:
        return f"No CVEs found for {service_banner} (not in mock database)"
