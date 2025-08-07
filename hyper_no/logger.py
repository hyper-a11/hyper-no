import datetime

def log_result(data):
    with open("scan.log", "a") as f:
        f.write("\n========== SCAN LOG ==========\n")
        f.write(f"Timestamp: {datetime.datetime.now()}\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
