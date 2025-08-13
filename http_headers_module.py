import requests

def fetch_http_headers(target):
    try:
        if not target.startswith("http://") and not target.startswith("https://"):
            target = "http://" + target

        response = requests.head(target, timeout=5)
        headers = response.headers

        result = f"HTTP Headers for {target}:\n\n"
        for key, value in headers.items():
            result += f"{key}: {value}\n"

        return result
    except requests.exceptions.RequestException as e:
        return f"[ERROR] Failed to fetch HTTP headers: {e}"

