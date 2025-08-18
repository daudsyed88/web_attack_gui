# modules/port_scanner_module.py
import socket

# common ports to scan safely
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389]

def run_port_scan(target):
    result_lines = [f"Port scan results for: {target}\n"]
    for port in COMMON_PORTS:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            status = s.connect_ex((target, port))
            if status == 0:
                result_lines.append(f"Port {port}: OPEN")
            else:
                result_lines.append(f"Port {port}: CLOSED")
            s.close()
        except Exception as e:
            result_lines.append(f"Port {port}: ERROR ({str(e)})")
    return "\n".join(result_lines)
