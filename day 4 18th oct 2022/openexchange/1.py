#Inspired by https://blog.teclado.com/how-to-interact-with-apis-using-python/
#Inspired by Python for Personal Finance
import requests
import json
# Create Python object from JSON string data
#obj = json.loads(json_data)
 
# Pretty Print JSON
#json_formatted_str = json.dumps(obj, indent=4)
#print(json_formatted_str)
#Manju Latest AppID
APP_ID = "cd3c41798514464bbc47d2e027806e25"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
#print(response.content)
currdata = json.loads(response.content)
 
# Pretty Print JSON
json_formatted_str = json.dumps(currdata, indent=4)
print(json_formatted_str)
# Writing to sample.json
with open("currency_table.json", "w") as outfile:
    outfile.write(json_formatted_str)