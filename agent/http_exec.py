#!/usr/bin/env python3
import sys, requests
def main():
    if len(sys.argv) < 3:
        print("Usage: http_exec.py <GET|POST> <url> [json_data]")
        sys.exit(1)
    method = sys.argv[1].upper()
    url = sys.argv[2]
    data = sys.argv[3] if len(sys.argv) > 3 else None
    headers = {"Content-Type": "application/json"}
    try:
        if method == "GET":
            resp = requests.get(url, timeout=10)
        elif method == "POST":
            resp = requests.post(url, data=data, headers=headers, timeout=10)
        else:
            print(f"Unsupported method: {method}")
            sys.exit(1)
        print(f"HTTP {method} {resp.status_code}")
        print(resp.text[:2000])
        sys.exit(0 if resp.ok else 1)
    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
