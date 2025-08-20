import socket

# Predefined wordlist of common domains to check against the target IP
COMMON_DOMAINS = [
    "example.com", "github.com", "python.org", "google.com",
    "wikipedia.org", "yahoo.com", "bing.com", "stackoverflow.com",
    "apple.com", "microsoft.com"
]

def run_reverse_ip_lookup(domain):
    """
    Resolves the target domain to an IP and finds other domains from COMMON_DOMAINS
    that share the same IP. No external API used.
    """
    try:
        ip = socket.gethostbyname(domain)
        results = []
        for d in COMMON_DOMAINS:
            try:
                if socket.gethostbyname(d) == ip:
                    results.append(d)
            except:
                continue
        return "\n".join(results) if results else f"No other domains found on IP {ip}"
    except Exception as e:
        return f"[ERROR] {str(e)}"
