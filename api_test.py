import urllib.request
import json

response = urllib.request.urlopen('https://api.restful-api.dev/objects')
data = json.loads(response.read())
print(json.dumps(data, indent=2))