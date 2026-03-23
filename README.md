# 🐞 Bug Bounty Automation Tool

A modular **Python-based Bug Bounty Tool** designed to automate reconnaissance and vulnerability scanning tasks. This tool helps security researchers and ethical hackers perform efficient domain analysis.

---

## 🚀 Features

* 🔍 Subdomain Enumeration
* 🌐 Port Scanning
* ⚠️ Basic Vulnerability Scanning
* 📄 Automated Report Generation
* 🧩 Modular Architecture (easy to extend)

---

## 📁 Project Structure

```
bugbounty_tool/
│
├── main.py                # Entry point of the application
├── readme.txt            # Documentation file
│
├── modules/
│   ├── subdomain.py      # Subdomain enumeration
│   ├── portscan.py       # Port scanning logic
│   ├── vulnscan.py       # Vulnerability scanning
│   └── report.py         # Report generation
│
├── reports/
│   └── output.txt        # Scan results
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/ashvikg/bugbounty_tool.git
cd bugbounty_tool
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the tool using:

```
python main.py
```

Enter the target domain when prompted.

---

## 🧠 Example

```
Enter target domain: example.com

[+] Finding subdomains...
[+] Scanning ports...
[+] Checking vulnerabilities...
[+] Generating report...

✅ Scan Completed!
```

---

## 📄 Output

* Results are saved in:

```
/reports/output.txt
```

---

## 🔥 Future Improvements

* CLI arguments support (`-d domain`)
* Integration with tools like:

  * subfinder
  * nmap
  * httpx
* JSON report export
* GUI dashboard (Flask or React)
* Live scanning progress

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.
Do not use it on systems without proper authorization.

---

## 👨‍💻 Author

Developed by Ashvik 🚀

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
