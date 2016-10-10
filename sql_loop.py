import sqlite3
import json



conn = sqlite3.connect("atm_numbers.sqlite")
c = conn.cursor()
c.execute('SELECT * FROM Ukraine order BY NUMBER')

for row in c:
    lat = row[11]
    lng = row[12]
    site = row[9]
    name = row[1]
    phone = row[10]
    address = row[5]
    city = row[3]


    print('r = requests.post(post_url, json={'
        '"location": {','\n',
    '"lat":' ,lat+',''\n',
    '"lng":', lng+'\n',
    "},",'\n',
    '"accuracy" : 50,','\n',
    '"name":', '"Банкомат '+name+'"'+",",'\n',
    '"phone_number":', '"'+phone+'"'+',''\n',
    '"address":', '"'+city+', '+address+'"'+',''\n',
    '"types": ["atm"]'+',''\n',
    '"website":', '"'+site+'"'+',''\n',
    '"language": "ru"''\n',
    '})''\n'
    'print(r.status_code)''\n'
    'print(r.json())'
    )


