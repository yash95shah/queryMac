import pprint 
import requests
import os

API_KEY=os.environ['API_K']
print ("**************************************************")
try:
    mac_id=input("Enter the mac-id that you want to search for (delimiters like ':','.' or no delimiters)- ") 
except EOFError as e:
    print (e)

try:
    r = requests.get('https://api.macaddress.io/v1?apiKey=' + API_KEY + '&output=json&search='+mac_id)
    st = r.json()
    print ("The mac id belongs to: - "+ st['vendorDetails']['companyName'])
except KeyError as k:
    print (k)
print ("**************************************************")
