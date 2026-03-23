#----Great Wall of Digital China----#
from typing import ItemsView
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
import urllib.request
import json
import uvicorn
import webbrowser
import ssl
from fastapi import FastAPI







app = FastAPI()
## creates a Key to skip the security certificate check 
ssl_context = ssl._create_unverified_context()

@app.get("/send_to_sheets")
async def send_to_sheets():
    url = "https://data.sugarlandtx.gov/datastore/odata3.0/cba72fda-a133-4f3e-88d2-d8ebcb901963?$top=5&$format=json"
    with urllib.request.urlopen(url, context= ssl_context) as response:
        raw_data = json.loads(response.read())
        items = raw_data.get('value',[])

    scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]##gives the script the permission to read and write data inside the google sheets 
    creds = ServiceAccountCredentials.from_json_keyfile_name("sugarland-data-project-53facb21cec7.json",scope)
    client = gspread.authorize(creds)
    sheet = client.open("Sugarland_data-project").sheet1
    for item in items:
        sheet.append_row(list(item.values()))
    return {"status": "success"}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.get("/sugarLand_data")## decoder that tells the FastAPi when someone visits the local host it runs the get_data() function
async def extract_data():
    url =  'https://data.sugarlandtx.gov/datastore/odata3.0/cba72fda-a133-4f3e-88d2-d8ebcb901963?$top=5&$format=json'
    with urllib.request.urlopen(url, context= ssl_context) as response:    #taking data from the API key
        data = json.loads(response.read())
    return data## coverts the data into Json

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000/docs")
    uvicorn.run (app, host="0.0.0.0", port=8000)

id = 'cba72fda-a133-4f3e-88d2-d8ebcb901963'
fileobj = urllib.request.urlopen("url")
response_dict = json.loads(fileobj.read())
print(response_dict)

extract_data()