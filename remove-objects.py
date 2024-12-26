import json

def remove_nested_objects():
    # Read the input JSON file
    with open('fixed_results.json', 'r') as file:
        data = json.load(file)
    
    # Remove drafts and suggestions from each record
    for record in data:
        if 'drafts' in record:
            del record['drafts']
        if 'suggestions' in record:
            del record['suggestions']
    
    # Write the flattened data back to a new file
    with open('results_flat.json', 'w') as file:
        json.dump(data, file, indent=2)

    print("Successfully removed nested objects and wrote results to results_flat.json")

if __name__ == "__main__":
    remove_nested_objects()
