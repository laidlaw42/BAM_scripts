"""
This Python script interacts with the BioNet NSW API to retrieve detailed information
about a specific Plant Community Type (PCT) based on its unique identifier (PCTID).
The API provides data in JSON format, and the script prompts the user to input
the target PCTID. It then constructs an API request to fetch and process the
information for the specified PCTID from the 'VegetationClassification_PCTDefinition'
entity set. The script efficiently filters the API response to retrieve only the
necessary data, enhancing performance by avoiding fetching the entire dataset.
The detailed properties of the PCT, such as institution code, collection code,
vegetation class, etc., are printed if information is found. If no information is
found, an appropriate message is displayed. This script is designed to facilitate
user queries for ecological and botanical details from the BioNet NSW dataset.
"""

import requests

def get_info_by_pctid(json_content, target_pctid):
    for entity in json_content:
        current_pctid = entity.get("PCTID")

        if current_pctid and int(current_pctid) == target_pctid:
            # Print all properties for the specific PCTID
            print(f"Information for PCTID {target_pctid}:")
            for prop_name, prop_value in entity.items():
                print(f"{prop_name}: {prop_value}")
            break  # Stop searching after finding the target PCTID
    else:
        print(f"No information found for PCTID {target_pctid}")

# Example usage
base_url = 'https://data.bionet.nsw.gov.au/biosvcapp/odata/'
entity_set = 'VegetationClassification_PCTDefinition'

try:
    # Prompt the user for the target PCTID
    target_pctid = int(input("Enter the target PCTID: "))

    # Fetch only the specific record using a filter in the API request
    api_url = f'{base_url}{entity_set}?$filter=PCTID eq {target_pctid}'
    json_content_response = requests.get(api_url)
    json_content_response.raise_for_status()

    json_content = json_content_response.json()

    if json_content["value"]:
        get_info_by_pctid(json_content["value"], target_pctid)
    else:
        print(f"No information found for PCTID {target_pctid}")

except requests.RequestException as e:
    print(f"Error during HTTP request: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
