import json
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python script_count.py <filename.json>")
    sys.exit(1)

filename = sys.argv[1]

# Check if file exists
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

# Load and count
try:
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, list):
        print("Total objects:", len(data))
    elif isinstance(data, dict):
        print("Total top-level keys:", len(data))
    else:
        print("Unsupported JSON structure.")
except Exception as e:
    print(f"Error reading JSON file: {e}")
