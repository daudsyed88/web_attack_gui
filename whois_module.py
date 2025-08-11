import whois

def run_whois_lookup(target):
    """
    Perform a WHOIS lookup for a given domain or IP.
    Returns formatted string output.
    """
    try:
        w = whois.whois(target)
        if not w:
            return "[INFO] No WHOIS information found."

        result = []
        for key, value in w.items():
            # Some values can be lists (like name servers), so join them
            if isinstance(value, list):
                value = ", ".join(map(str, value))
            result.append(f"{key}: {value}")

        return "\n".join(result)
    except Exception as e:
        return f"[ERROR] Whois lookup failed: {str(e)}"
