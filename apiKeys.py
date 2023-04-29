import requests
import json
import random

header_array = ['BARCODE', 'DATE', 'TIME', '24V_PU', '5V_PU', 'RPL_PU', '24V_NL', '5V_NL', 'RPL_NL', 'SW', 
'LPS_FLT', 'DCAL', 'SV_PUMP', '24V_SV', '5V_SV', 'RPL_SV', '24V_90V', 
'5V_90V', 'RPL_90V', '24V_265V', '5V_265V', 'RPL_265V', 'HICUT', 'HC_RCVRY', 'UV', 'UV_FPH', 'UV_FON', 'UV_IPH', 'UV_ION', 'UV_DUTPR', 'UV_DUTON', '24V_FL', '5V_FL', 'RPL_FL', 'FINAL_CODE', 'DUMMY1', 'DUMMY2', 'DUMMY3', 'TEST_STATUS']
api_key = "ys8RM6oGh9f3lfq5dXXb3JQnCEUWJ9QRbJnm2chdWxqDQnNpX8Ai9uxSo8zkC8Zk"
url = "https://data.mongodb-api.com/app/data-kbvif/endpoint/data/v1/action/insertOne"

# Define the data to be inserted

result=["pass","fail"]
data = [
    {
        header_array[0]: random.randint(1,20),
        header_array[1]: random.randint(1,20),
        header_array[2]: random.randint(1,20),
        header_array[3]: random.randint(1,20),
        header_array[5]:random.randint(1,20),
        header_array[6]: random.randint(1,20),
        header_array[7]: random.randint(1,20),
        header_array[8]: random.randint(1,20),
        header_array[9]: random.randint(1,20),
        header_array[10]: random.randint(1,20),
        header_array[11]: random.randint(1,20),
        header_array[12]: random.randint(1,20),
        header_array[13]: random.randint(1,20),
        header_array[14]: random.randint(1,20),
        header_array[15]: random.randint(1,20),
        header_array[16]: random.randint(1,20),
        header_array[17]: random.randint(1,20),
        header_array[18]: random.randint(1,20),
        header_array[19]: random.randint(1,20),
        header_array[20]: random.randint(1,20),
        header_array[21]: random.randint(1,20),
        header_array[22]: random.randint(1,20),
        header_array[23]: random.randint(1,20),
        header_array[24]: random.randint(1,20),
        header_array[25]: random.randint(1,20),
        header_array[26]: random.randint(1,20),
        header_array[27]: random.randint(1,20),
        header_array[28]: random.randint(1,20),
        header_array[29]: random.randint(1,20),
        header_array[30]: random.randint(1,20),
        header_array[31]: random.randint(1,20),
        header_array[32]: random.randint(1,20),
        header_array[33]: random.randint(1,20),
        header_array[34]: random.randint(1,20),
        header_array[35]: random.randint(1,20),
        header_array[36]: random.choices(result),
         header_array[37]: "mac"
    },
    {
       header_array[0]: random.randint(1,20),
        header_array[1]: random.randint(1,20),
        header_array[2]: random.randint(1,20),
        header_array[3]: random.randint(1,20),
        header_array[5]:random.randint(1,20),
        header_array[6]: random.randint(1,20),
        header_array[7]: random.randint(1,20),
        header_array[8]: random.randint(1,20),
        header_array[9]: random.randint(1,20),
        header_array[10]: random.randint(1,20),
        header_array[11]: random.randint(1,20),
        header_array[12]: random.randint(1,20),
        header_array[13]: random.randint(1,20),
        header_array[14]: random.randint(1,20),
        header_array[15]: random.randint(1,20),
        header_array[16]: random.randint(1,20),
        header_array[17]: random.randint(1,20),
        header_array[18]: random.randint(1,20),
        header_array[19]: random.randint(1,20),
        header_array[20]: random.randint(1,20),
        header_array[21]: random.randint(1,20),
        header_array[22]: random.randint(1,20),
        header_array[23]: random.randint(1,20),
        header_array[24]: random.randint(1,20),
        header_array[25]: random.randint(1,20),
        header_array[26]: random.randint(1,20),
        header_array[27]: random.randint(1,20),
        header_array[28]: random.randint(1,20),
        header_array[29]: random.randint(1,20),
        header_array[30]: random.randint(1,20),
        header_array[31]: random.randint(1,20),
        header_array[32]: random.randint(1,20),
        header_array[33]: random.randint(1,20),
        header_array[34]: random.randint(1,20),
        header_array[35]: random.randint(1,20),
        header_array[36]: random.choices(result),
         header_array[37]: "mac"
    }
]

# Create the JSON payload for the API request
payload = json.dumps({
    "collection": "test1",
    "database": "capacity_test",
    "dataSource": "Cluster0",
    "documents": data
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