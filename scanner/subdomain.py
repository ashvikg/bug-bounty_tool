# scanner/subdomain.py
import requests
from scanner.report import save_report

def find_subdomains(domain):
    subdomains = ["www", "mail", "ftp", "admin", "api"]
    found = []

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"[FOUND] {url}")
            save_report(f"[FOUND] {url}")
        except:
            pass

    return found
    