import requests
import pandas as pd
from io import StringIO
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

password=os.getenv("password")
client_secret=os.getenv("client_secret")
client_id=os.getenv("client_id")
username=os.getenv("username")

params = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password,
}

# use the test.salesforce.com domain for sandbox authentication
r = requests.post("https://login.salesforce.com/services/oauth2/token", params=params)

access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")

print(access_token)
print(instance_url)

#prework for the script: use the SOQL query to get a list of endpoints
#manipulate that SOQL response into an array of endpoints. then you will query all of those endpoints in the below function

endpoints=['/services/data/v54.0/sobjects/EventLogFile/[yourIDhere]/LogFile',]

def get_sfdc_responses():

    payload={}
    headers = {
        'Authorization': 'Bearer %s' % f'{access_token}',
        'Content-type': 'application/json'
    }
    for i in range(len(endpoints)):
        #configure the domain/org that you are using for the endpoints
        apiURL = "https://example.my.salesforce.com{}".format(endpoints[i])

        response = requests.request("GET", apiURL, headers=headers, data=payload)
        report = response.content.decode("utf-8")

        #using pandas and dataframes to take the responses and convert to csv files
        df = pd.read_csv(StringIO(report))

        #define the directory that you want to save the files in
        #each of the files has it's index appended in the file name in order to differentiate
        df.to_csv('/Users/Desktop/CSV/out-{}.csv'.format(i))

#call function
get_sfdc_responses()