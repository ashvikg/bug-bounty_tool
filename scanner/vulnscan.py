import requests
from scanner.report import save_report

def scan_xss(url):
    payload = "<script>alert(1)</script>"
    test_url = f"http://{url}?q={payload}"

    try:
        r = requests.get(test_url)
        if payload in r.text:
            print("[VULNERABLE] XSS Found!")
            save_report("[VULNERABLE] XSS Found on " + url)
    except:
        pass


def scan_sqli(url):
    payload = "' OR '1'='1"
    test_url = f"http://{url}?id={payload}"

    try:
        r = requests.get(test_url)
        errors = ["sql", "syntax", "mysql"]

        for error in errors:
            if error in r.text.lower():
                print("[VULNERABLE] SQL Injection Found!")
                save_report("[VULNERABLE] SQLi Found on " + url)
                break
    except:
        pass