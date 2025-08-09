# modules/nmap_module.py
import nmap

def run_nmap_scan(target, scan_type="quick"):
    nm = nmap.PortScanner()

    try:
        if scan_type == "quick":
            nm.scan(target, arguments="-F")  # Fast scan (common ports)
        elif scan_type == "full":
            nm.scan(target, arguments="-p-")  # Scan all ports
        else:
            nm.scan(target)  # Default scan

        output = []
        for host in nm.all_hosts():
            output.append(f"Host: {host} ({nm[host].hostname()})")
            output.append(f"State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    service = nm[host][proto][port]['name']
                    output.append(f"Port: {port}\tService: {service}")

        return "\n".join(output)

    except Exception as e:
        return f"[ERROR] {e}"
