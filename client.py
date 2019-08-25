import requests
import json

url = 'http://localhost:8080/imports'
headers = {'Content-Type': 'application/json'}
body_post = """{
  "citizens": [
    {
      "citizen_id": 1,
      "town": "Москва",
      "street": "Льва Толстого",
      "building": "16к7стр5",
      "apartment": 7,
      "name": "Иванов Иван Иванович",
      "birth_date": "26.12.1986",
      "gender": "male",
      "relatives": [
        2
      ]
    },
    {
      "citizen_id": 2,
      "town": "Москва",
      "street": "Льва Толстого",
      "building": "16к7стр5",
      "apartment": 7,
      "name": "Иванов Сергей Иванович",
      "birth_date": "01.04.1997",
      "gender": "male",
      "relatives": [
        1, 4
      ]
    },
    {
      "citizen_id": 3,
      "town": "Керчь",
      "street": "Иосифа Бродского",
      "building": "2",
      "apartment": 11,
      "name": "Романова Мария Леонидовна",
      "birth_date": "23.11.1986",
      "gender": "female",
      "relatives": []
    }, 
     {
      "citizen_id": 4,
      "town": "Керчь",
      "street": "Иосифа Бродского",
      "building": "2",
      "apartment": 11,
      "name": "Романова Мария Леонидовна",
      "birth_date": "23.11.1986",
      "gender": "female",
      "relatives": [2]
    }
  ]
}"""

req = requests.post(url, headers=headers, data=body_post.encode('utf-8'))

print(req.status_code)
print(req.headers)
print(req.text)
print("-"*20)


req = requests.get(url + "/0/citizens")

print(req.status_code)
print(req.headers)
print(req.text)
print("-"*20)


body_patch = """{
"name": "Иванова Мария Леонидовна",
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"relatives": [1]
}
"""


req = requests.patch(url + "/0/citizens/3", headers=headers, data=body_patch.encode('utf-8'))

print(req.status_code)
print(req.headers)
print(req.text)
print("-"*20)

req = requests.get(url + "/0/citizens/birthdays")

print(req.status_code)
print(req.headers)
print(req.text)
print("-"*20)

req = requests.get(url + "/0/towns/stat/percentile/age")

print(req.status_code)
print(req.headers)
print(req.text)

