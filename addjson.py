
import urllib.request
import json

body = {
  "location": {
    "lat": 50.4494061,
    "lng": 30.4588717
  },
  "accuracy": 50,
  "name": "Креди Агриколь",
  "phone_number": "+380 44 495 22 77",
  "address": "Киев, пр. Победы, 37",
  "types": ["ATM"],
  "website": "https://credit-agricole.ua/",
  "language": "ru"
    }

myurl = "https://maps.googleapis.com/maps/api/place/add/json?key=AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print(jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
print(response.read)
print(response)

s = response.read
print (s)
