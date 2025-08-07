import json
import csv

def export_to_json(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename="output.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())

def export_to_txt(data, filename="output.txt"):
    with open(filename, "w") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
