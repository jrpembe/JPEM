# Application Programming Interface

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# Basic print of response produces a very messy result
# print(response.json())

# Using a built in json function we can clean up the result
# print(json.dumps(response.json(), indent = 2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])
