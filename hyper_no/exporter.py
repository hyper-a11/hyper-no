import json
import csv

def export_to_json(data):
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(data):
    with open("output.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])

def export_to_txt(data):
    with open("output.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
