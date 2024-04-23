# NSW Bionet API Data Retrieval Script

## Overview

Simple scripts that interact with the NSW Bionet API to retrieve datasets related to vegetation classifications. They specifically target PCT Definition, Growth Form Group, and PCT Benchmarks entity sets from [BioNet](https://data.bionet.nsw.gov.au/biosvcapp/odata). Changes and updates to come.

## Functionality

The script performs the following tasks:

1. **API Interaction**: Sends an HTTP GET request to the NSW Bionet API to fetch a specified dataset e.g.  "VegetationClassification_PCTGrowthForm".

3. **Data Retrieval & Storage**: Upon receiving the response, the script extracts and stores the content as a JSON. It also checks for updates and amends changes if the dataset is already stored. 

3. **Error Handling**: The script includes error handling to manage potential issues during the HTTP request, data extraction, and file saving processes. It provides informative error messages to assist in troubleshooting.

## Requirements

- Python 3.x
- `requests` 
