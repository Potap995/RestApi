import requests
import json


# r = requests.post('http://localhost:8080/imports', data=json.dumps({'key':'value'}), headers={"Content-Type":"applicarion/json"})
# print(r.text)
r = requests.get('http://localhost:8080/imports' + '/' + '5d5d79621bcc4aca1ac7c1e3' + '/citizens')
print(r.text)