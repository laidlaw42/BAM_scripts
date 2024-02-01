"""
This Python script interacts with the NSW Bionet API to retrieve information about vegetation classifications.
It follows these steps:

1. Fetches the metadata to identify the available datasets and their structure.
2. Requests the actual dataset (JSON format) from the specified entity set, in this case,
   'VegetationClassification_PCTBenchmarks'.
3. Compares the current dataset with the previously stored dataset (if available).
4. If changes are detected, it updates the stored dataset with the current one.
5. Prompts the user to enter a target PCTID and displays detailed information if found.

Functions:
- save_dataset(data, filename='dataset_benchmarks.json'): Saves the provided dataset to a JSON file
  (default filename: 'dataset_benchmarks.json').
- load_dataset(filename='dataset.json'): Loads the dataset from a JSON file (default filename: 'dataset_benchmarks.json').
- get_info_by_pctid(data, target_pctid): Retrieves and prints information for a specified PCTID from the given dataset.

Note: Ensure you have the 'requests' library installed (you can install it using 'pip install requests').
"""

import requests
import json
import os


def save_dataset(data, filename='dataset_benchmarks.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_dataset(filename='dataset_benchmarks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def get_info_by_pctid(data, target_pctid):
    for entity in data:
        current_pctid = entity.get('PCTID')

        if current_pctid and int(current_pctid) == target_pctid:
            # Extract information for the specific PCTID
            print(f"Information for PCTID {target_pctid}:")
            for key, value in entity.items():
                print(f"{key}: {value}")
            break  # Stop searching after finding the target PCTID
    else:
        print(f"No information found for PCTID {target_pctid}")


# Example usage
base_url = 'https://data.bionet.nsw.gov.au/biosvcapp/odata/'
entity_set = 'VegetationClassification_PCTBenchmarks'
metadata_url = f'{base_url}$metadata'

try:
    metadata_response = requests.get(metadata_url)
    metadata_response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

    json_content_response = requests.get(f'{base_url}{entity_set}')
    json_content_response.raise_for_status()

    current_data = json_content_response.json().get('value', [])

    if not current_data:
        raise ValueError("Empty or invalid JSON content received.")

    # Load the previously stored dataset
    stored_data = load_dataset()

    # Compare current and stored datasets
    if current_data != stored_data:
        print("Benchmark dataset has been updated. Saving the new dataset.")
        save_dataset(current_data)
    else:
        print("No changes detected in the dataset.")

    # Prompt the user for the target PCTID
    target_pctid = int(input("Enter the target PCTID: "))

    get_info_by_pctid(current_data, target_pctid)

except requests.RequestException as e:
    print(f"Error during HTTP request: {e}")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
