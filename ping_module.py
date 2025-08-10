# modules/ping_module.py
import subprocess

def run_ping(target):
    try:
        # Ping 4 times (-c 4 for Linux)
        result = subprocess.run(
            ["ping", "-c", "4", target],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"[ERROR] Ping failed:\n{result.stderr}"
    except Exception as e:
        return f"[EXCEPTION] {e}"
