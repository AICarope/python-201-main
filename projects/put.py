#PUT API call

import requests
import json 
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[YOUR UPDATED FIELD]",
    "last_name": "[YOUR UPDATED FIELD]",
    "email": "[YOUR EMAIL]"
}

# here we execute the PUT request
response = requests.put(base_url + "/YOUR_ID", json=body)
# print the status code (hopefully it's 200 which means all is well)
mydata = response.text
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")
with open('data.json', 'w') as f:
    json.dump(mydata, f, indent=4)

print(response.text)
##