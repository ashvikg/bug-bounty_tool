def save_report(message):
    with open("reports/output.txt", "a") as f:
        f.write(message + "\n")