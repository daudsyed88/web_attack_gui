import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return f"[+] Domain: {domain}\n[+] IP Address: {ip}"
    except Exception as e:
        return f"[!] Error performing DNS Lookup: {str(e)}"
