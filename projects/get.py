#GET API call
import requests
import json 
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
mydata = response.text
#print(response.status_code)
with open('data.json', 'w') as f:
    json.dump(mydata, f, indent=4)

print(response.text)