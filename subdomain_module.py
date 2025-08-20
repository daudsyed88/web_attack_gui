import dns.resolver
import aiohttp
import asyncio

WORDLIST_FILE = "modules/subdomains.txt"

async def fetch(session, url):
    try:
        async with session.get(f"http://{url}", timeout=5) as response:
            return url, response.status
    except:
        return url, None

async def scan_subdomains(domain):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        with open(WORDLIST_FILE) as f:
            for sub in f.read().splitlines():
                sub = sub.strip()
                if sub:
                    full = f"{sub}.{domain}"
                    try:
                        dns.resolver.resolve(full, 'A')  # check DNS
                        tasks.append(fetch(session, full))  # check HTTP
                    except:
                        pass
        for future in asyncio.as_completed(tasks):
            url, status = await future
            if status:
                results.append(f"{url} -> {status}")
            else:
                results.append(f"{url} -> DNS exists, no HTTP response")
    return "\n".join(results) if results else "No subdomains found."

def run_subdomain_scan(domain):
    return asyncio.run(scan_subdomains(domain))
