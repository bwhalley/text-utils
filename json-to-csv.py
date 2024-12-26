import json
import csv

def convert_json_to_csv():
    # Read the JSON file
    with open('results_flat_cleaned.json', 'r') as json_file:
        data = json.load(json_file)
    
    if not data:
        print("No data found in JSON file")
        return
        
    # Get headers from first 5 records (or all if less than 5)
    sample_size = min(5, len(data))
    headers = set()
    for i in range(sample_size):
        headers.update(data[i].keys())
    headers = sorted(list(headers))  # Convert to sorted list for consistent column order
    
    # Write to CSV
    with open('results_flat.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        
        # Write headers
        writer.writeheader()
        
        # Write data rows
        writer.writerows(data)
        
    print(f"Successfully converted {len(data)} records to CSV")

if __name__ == "__main__":
    convert_json_to_csv()
