import requests
import json

header_array = ['BARCODE', 'DATE', 'TIME', '24V_PU', '5V_PU', 'RPL_PU', '24V_NL', '5V_NL', 'RPL_NL', 'SW', 'LPS_FLT', 'DCAL', 'SV_PUMP', '24V_SV', '5V_SV', 'RPL_SV', '24V_90V', '5V_90V', 'RPL_90V', '24V_265V', '5V_265V', 'RPL_265V', 'HICUT', 'HC_RCVRY', 'UV', 'UV_FPH', 'UV_FON', 'UV_IPH', 'UV_ION', 'UV_DUTPR', 'UV_DUTON', '24V_FL', '5V_FL', 'RPL_FL', 'FINAL_CODE', 'DUMMY1', 'DUMMY2', 'DUMMY3', 'TEST_STATUS']
api_key = "ys8RM6oGh9f3lfq5dXXb3JQnCEUWJ9QRbJnm2chdWxqDQnNpX8Ai9uxSo8zkC8Zk"
url = "https://data.mongodb-api.com/app/data-kbvif/endpoint/data/v1/action/insertOne"

# Define the data to be inserted
data = [
    {
        header_array[0]: "ABC123",
        header_array[1]: "2021-01-01",
        header_array[2]: "10:00:00",
        header_array[3]: 1.0,
        header_array[4]: 2.0,
        # ...
        header_array[-1]: "PASS"
    },
    {
        header_array[0]: "DEF456",
        header_array[1]: "2021-01-02",
        header_array[2]: "11:00:00",
        header_array[3]: 2.0,
        header_array[4]: 3.0,
        # ...
        header_array[-1]: "FAIL"
    }
]

# Create the JSON payload for the API request
payload = json.dumps({
    "collection": "test1",
    "database": "capacity_test",
    "dataSource": "Cluster0",
    "documents": [
        {
            "BARCODE": "123456",
            "DATE": "2023-01-21",
            "TIME": "12:00:00",
            # Add the rest of the values from the header_array
        }
    ]
})
# Set the request headers
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': api_key,
}

# Make the API request to insert the data
response = requests.post(url, headers=headers, data=payload)

# Check the response status code to see if the request was successful
if response.status_code == 200:
    print("Data was uploaded successfully")
else:
    print("Error uploading data: " + response.text)
