# scanner/portscan.py
import socket
from scanner.report import save_report

def scan_ports(host):
    ports = [21, 22, 80, 443, 3306]

    for port in ports:
        s = socket.socket()
        s.settimeout(1)

        try:
            s.connect((host, port))
            print(f"[OPEN] Port {port}")
            save_report(f"[OPEN] Port {port} on {host}")
        except:
            pass

        s.close()