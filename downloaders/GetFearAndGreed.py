import json
import csv

# Load data from greedfear.json
with open('data/json/fearandgreed.json', 'r') as f:
    data = json.load(f)

# Extract date and GreedFearIndex columns
extracted_data = [[item[0], round(float(item[1]), 2)] for item in data]

# Save to CSV file
with open('data/csv/data_fearandgreed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "FearAndGreedIndex"])  # header row
    writer.writerows(extracted_data)


