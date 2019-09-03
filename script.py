import pprint 
import requests
import os

API_KEY= os.getenv('API_K')
mac_id=input("Enter the mac-id that you want to search for - (You can use octet delimiters including ':', '.' or even no delimiter)") 

r = requests.get('https://api.macaddress.io/v1?apiKey=' + API_KEY + '&output=json&search='+mac_id)
st = r.json()

pprint.pprint (st['vendorDetails']['companyName'])