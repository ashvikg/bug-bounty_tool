# main.py
from scanner.subdomain import find_subdomains
from scanner.portscan import scan_ports
from scanner.vulnscan import scan_xss, scan_sqli

target = input("Enter target (example.com): ")

print("\n[+] Finding subdomains...")
subs = find_subdomains(target)

print("\n[+] Scanning ports...")
scan_ports(target)

print("\n[+] Testing vulnerabilities...")
scan_xss(target)
scan_sqli(target)

print("\n[✓] Scan Completed!")
