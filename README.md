# NSW Bionet API Data Retrieval Script

## Overview

This Python script interacts with the NSW Bionet API to retrieve datasets related to vegetation classifications. It specifically targets the PCT Definition, Growth Form Group, and PCT Benchmarks entity sets from [BioNet](https://data.bionet.nsw.gov.au/biosvcapp/odata).

## Functionality

The script performs the following tasks:

1. **API Interaction**: It sends an HTTP GET request to the NSW Bionet API to fetch the dataset associated with the "VegetationClassification_PCTGrowthForm" entity set.

2. **Data Retrieval**: Upon receiving the response, the script extracts the JSON content containing information about vegetation growth forms.

3. **Data Storage**: The retrieved dataset is saved to a local JSON file named "growth_form_dataset.json" for future reference and analysis.

4. **Error Handling**: The script includes error handling to manage potential issues during the HTTP request, data extraction, and file saving processes. It provides informative error messages to assist in troubleshooting.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Usage

1. Ensure Python 3.x is installed on your system.
2. Install the required `requests` library using `pip install requests`.
3. Run the script using the following command: `python SCRIPTNAME.py`
4. The script will retrieve the dataset from the NSW Bionet API and save it to a local JSON file named "growth_form_dataset.json" in the same directory.

## Additional Notes

- Ensure an active internet connection to access the NSW Bionet API.
- Review the API documentation for further information on available endpoints and data structures.
