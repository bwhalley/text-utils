import json

# Read the input file
with open('results_flat.json', 'r') as f:
    data = json.load(f)

# Filter out error records
cleaned_data = [record for record in data if 'error' not in record]

# Write cleaned data to new file
with open('results_flat_cleaned.json', 'w') as f:
    json.dump(cleaned_data, f, indent=2)
