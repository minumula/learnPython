import requests
import json

response = requests.get('https://freegeoip.app/json/')
json_response = response.json()

#print (response.status_code)
print(response.json())

Country = json_response['country_name']
StateName = json_response['region_name']
City = json_response['city']

print (json_response['country_name'])
print (StateName)
print (City)

