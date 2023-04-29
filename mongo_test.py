
from pymongo import MongoClient
import random
client = MongoClient("mongodb+srv://Adarsh:terrorbull@2021@cluster0.0vbjflg.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('capacity_test')
collection = db['test1']

header_array = ['BARCODE', 'DATE', 'TIME', '24V_PU', '5V_PU', 'RPL_PU', '24V_NL', '5V_NL', 'RPL_NL', 'SW', 
'LPS_FLT', 'DCAL', 'SV_PUMP', '24V_SV', '5V_SV', 'RPL_SV', '24V_90V', 
'5V_90V', 'RPL_90V', '24V_265V', '5V_265V', 'RPL_265V', 'HICUT', 'HC_RCVRY', 'UV', 'UV_FPH', 'UV_FON', 'UV_IPH', 'UV_ION', 'UV_DUTPR', 'UV_DUTON', '24V_FL', '5V_FL', 'RPL_FL', 'FINAL_CODE', 'DUMMY1', 'DUMMY2', 'DUMMY3', 'TEST_STATUS']


count = collection.count_documents({})
cin=0

while(True):

    result=["pass","fail"]
    data = {
        header_array[0]: random.random(),



        header_array[1]: random.random(),



        header_array[2]: random.random(),



        header_array[3]: random.random(),



        header_array[5]:random.random(),



        header_array[6]: random.random(),



        header_array[7]: random.random(),



        header_array[8]: random.random(),



        header_array[9]: random.random(),



        header_array[10]: random.random(),



        header_array[11]: random.random(),



        header_array[12]: random.random(),



        header_array[13]: random.random(),



        header_array[14]: random.random(),



        header_array[15]: random.random(),



        header_array[16]: random.random(),



        header_array[17]: random.random(),



        header_array[18]: random.random(),



        header_array[19]: random.random(),



        header_array[20]: random.random(),



        header_array[21]: random.random(),



        header_array[22]: random.random(),



        header_array[23]: random.random(),



        header_array[24]: random.random(),



        header_array[25]: random.random(),



        header_array[26]: random.random(),



        header_array[27]: random.random(),



        header_array[28]: random.random(),



        header_array[29]: random.random(),



        header_array[30]: random.random(),



        header_array[31]: random.random(),



        header_array[32]: random.random(),



        header_array[33]: random.random(),



        header_array[34]: random.random(),



        header_array[35]: random.random(),



        header_array[36]: random.choices(result),
         header_array[37]: "mac"
        }

    collection.insert_one(data)
    cin=cin+1

    print("Document inserted successfully")
    print("the count of document is",cin)

# document["_id"]=input("enter thr number :")
# # collection.insert_one(document)
print("Document inserted successfully")






print("Number of documents in the collection: ", count)

print(collection)