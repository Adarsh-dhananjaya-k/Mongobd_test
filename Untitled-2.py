import requests
import json
url = "https://data.mongodb-api.com/app/data-kbvif/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "test1",
    "database": "capacity_test",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
                 },
    "documents": [
        {
            "BARCODE": "123456",
            "DATE": "2023-01-21",
            "TIME": "12:00:00",
          
        }
    ]
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'b6FjsoEw9m1hAaLdsSfcmtccnaIJe4eKcQynAnJc183tdK4Jv0Rvlir9aRlYNAT5', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
