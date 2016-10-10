import requests

post_url = "https://maps.googleapis.com/maps/api/place/add/json?key=AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag"

r = requests.post(post_url, json={"location": {
 "lat": 46.967412,
 "lng": 31.974406
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Центральный, 27 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.54921,
 "lng": 30.196937
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Буча, ул. Новое шоссе, 48",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.261434,
 "lng": 35.324574
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Пришиб, ул. Ленина, 95 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.622567,
 "lng": 31.100708
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Южный, пр. Григорьевского десанта",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.433124,
 "lng": 30.702252
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Генерала Петрова, 51",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.18743,
 "lng": 30.345941
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Белгород-Днестровский, ул. Лазо, 28",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.56673,
 "lng": 30.777545
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Добровольского, 70 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.668749,
 "lng": 31.212915
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ленинка, ул. Виноградная, 2 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.477158,
 "lng": 34.913209
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Метростроевская, 19",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.971092,
 "lng": 31.991565
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, ул. Советская, 3",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.950899,
 "lng": 31.942586
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, ул. Озерная, 13В/3",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.431854,
 "lng": 30.708484
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Генерала Петрова, 22",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.406168,
 "lng": 30.711624
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Маршала Жукова, 65 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.300121,
 "lng": 30.656503
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ильичевск, ул. 1-го Мая, 3 Р",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.436558,
 "lng": 35.068546
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Набережная Победы, 56",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.937345,
 "lng": 33.434469
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, бул. Вечерний, 33",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.465687,
 "lng": 35.046739
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, бул. Европейский, 1 Д",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.460384,
 "lng": 30.704329
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Мельницкая, 13",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.964459,
 "lng": 33.436613
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пр. 200-летия Кривого Рога, 7 Д",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, пр. Ленина, 192",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.928701,
 "lng": 35.083193
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Владимировское, ул. Космическая, 12 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.783291,
 "lng": 35.207491
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Парамонова, 15",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.907902,
 "lng": 33.419122
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пр. Гагарина, 69",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.899792,
 "lng": 33.393265
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пр. Металлургов, 9/65",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.433013,
 "lng": 35.002204
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Титова, 36",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.477026,
 "lng": 35.021396
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Пастера, 12",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.755519,
 "lng": 25.289216
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Луцк, ул. Ковельская, 150",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.909779,
 "lng": 33.393933
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пр. Гагарина, 4 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.446132,
 "lng": 35.031566
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск,  ул. Сечевых стрельцов, 91",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.479893,
 "lng": 34.991448
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Ударников, 42",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.984119,
 "lng": 36.341724
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, пр. Тракторостроителей, 59/56",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.964981,
 "lng": 32.011243
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Центральный, 157",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.908563,
 "lng": 33.341697
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пл. Освобождения, 1 К",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.434473,
 "lng": 30.76076
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Генуэзская, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.938033,
 "lng": 32.039239
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Богоявленский, 55",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.6024578,
 "lng": 34.5996529
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Елизаветовка, ул. Тепличная, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.458042,
 "lng": 30.75736
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, бул. Французский, 16",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.485974,
 "lng": 30.743788
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пл. Думская, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.967752,
 "lng": 32.022279
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, ул. Слободская, 6",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.399129,
 "lng": 30.730168
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Академика Глушко, 1/3",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.465658,
 "lng": 30.722578
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Болгарская, 38",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.47095,
 "lng": 30.763295
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пляж Аркадия, 25",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.571992,
 "lng": 30.779022
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Добровольского, 71",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.56939,
 "lng": 30.79013
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Днепропетровская дорога, 74",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.95412,
 "lng": 36.380878
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, пр. Московский, 275",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.5639644,
 "lng": 30.833497
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Фонтанка, ТЦ Ривьера",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.756572,
 "lng": 33.37513
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Новая Каховка, ул. Парижской комуны, 55",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.471342,
 "lng": 30.726674
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Мечникова, 104",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.486846,
 "lng": 30.732528
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Елисаветинская, 18",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 54.947036,
 "lng": 37.417205
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Авангард, ул. Базовая, 20",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.438839,
 "lng": 35.051236
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Марии Кюри, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.463375,
 "lng": 35.03725
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Воскресенская, 36",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.594551,
 "lng": 30.802871
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Добровольского, 130/5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.018286,
 "lng": 36.225519
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, пр. Науки, 23",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.404971,
 "lng": 35.031912
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, Запорожское шоссе, 56",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.3679589,
 "lng": 30.6364128
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Малодолинское, ул. Винокурова, 9",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.597927,
 "lng": 31.306363
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Смолино, ул. Козакова, 41",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.528623,
 "lng": 35.870134
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Павлоград, ул. Центральная, 82",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.511715,
 "lng": 35.075769
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Калиновая, 14",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.511259,
 "lng": 34.992441
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, Донецкое шоссе, 9 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.151971,
 "lng": 30.541508
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Каролино-Бугаз, ул. Приморская, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.523899,
 "lng": 32.117238
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кировоград, пл. Дружби народов, 6",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.941276,
 "lng": 33.413714
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Мелешкина, 25",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.469838,
 "lng": 35.049605
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Европейская, 30",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.833086,
 "lng": 24.014117
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Львов, ул. Генерала Чупринки, 11",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.901138,
 "lng": 33.408115
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Косиора, 51",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.5639644,
 "lng": 30.833497
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Фонтанка, Фонтанка, ТЦ Ривьера",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.887337,
 "lng": 35.162634
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Историческая, 22",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.827696,
 "lng": 35.019302
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Маршала Судця, 26",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.489627,
 "lng": 31.276806
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Чернигов, ул. Щорса, 36",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.471649,
 "lng": 32.302314
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кировоград, ул. 50-летия Октября, 1 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.483764,
 "lng": 35.06395
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Маршала Малиновского, 2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.407606,
 "lng": 35.000073
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Богдана Хмельницкого, 118 Д",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.971692,
 "lng": 31.984721
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, ул. Пушкинская, 14/3",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.654665,
 "lng": 32.608184
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, пр. Ушакова, 70 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.433864,
 "lng": 30.761965
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Гагаринское плато, 5 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.456808,
 "lng": 30.731202
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Бассейная, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.194838,
 "lng": 30.352113
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Белгород-Днестровский, ул. Ленина, 44",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.435352,
 "lng": 30.729792
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Краснова, 6/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.6015553,
 "lng": 31.2858852
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Смолино, пгт. Смолино (шахта)",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.819362,
 "lng": 35.0494
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, пр. Юбилейный, 22 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.795938,
 "lng": 30.11497
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Белая Церковь, пл. Торговая, 2/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.855468,
 "lng": 32.013867
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Корабелов, 14",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.946081,
 "lng": 32.051216
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Мира, 40 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.955385,
 "lng": 32.038346
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, пр. Мира, 2 ",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.472652,
 "lng": 30.74188
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Большая Арнаутская, 32",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.478902,
 "lng": 30.732301
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Еврейская, 58",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.844135,
 "lng": 35.227943
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Волшебная, 155 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.900911,
 "lng": 33.343399
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Ленина, 55",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.840322,
 "lng": 33.34696
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, пр. Южный, 27/35",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.413427,
 "lng": 35.044312
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Космическая, 25 Д",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.537666,
 "lng": 32.268703
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кировоград, ул. Добровольского, 15",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.7308126,
 "lng": 33.6194473
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Нива Трудовая, ул. Ленина, 6",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.444543,
 "lng": 30.705274
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. И. Рабина, 2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.422324,
 "lng": 35.063062
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, пр. Героев, 1 С",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.652037,
 "lng": 32.644194
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, ул. Черноморская, 25",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.495464,
 "lng": 31.293682
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Чернигов, пр. Мира, 35",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.883753,
 "lng": 35.016425
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Рустави, 1 Г",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.433361,
 "lng": 30.722622
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Академика Филатова, 13",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.293324,
 "lng": 30.63807
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ильичевск, Ильичевск",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.033529,
 "lng": 33.476538
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Мусоргского, 17",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.780546,
 "lng": 35.184424
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Новокузнецкая, 12 В",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.484567,
 "lng": 30.73919
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Екатерининская, 17",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.664135,
 "lng": 32.600681
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, пр. 200-летия Херсона, 8",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.918689,
 "lng": 36.281326
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, ул. Ромашкина, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.987082,
 "lng": 36.209265
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, ул. Полтавский шлях, 56/58",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.95412,
 "lng": 36.380878
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, пр. Московский, 275",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.9935,
 "lng": 36.230383
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Харьков, ул. Боголея, 7",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.83884,
 "lng": 24.029183
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Львов, пл. Мицкевича, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.4730531,
 "lng": 32.1870801
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Соколовское, ул. Шоссейная, 3",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.074425,
 "lng": 33.515226
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Косыгина, 1 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.193021,
 "lng": 30.338977
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Белгород-Днестровский, ул. Измаильская, 60",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.390508,
 "lng": 30.720625
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Академика Вильямса, 75",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.832016,
 "lng": 23.993975
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Львов, ул. Полищука, 78 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.999002,
 "lng": 25.856018
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Заводское, ул. Ивана Франка, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.434597,
 "lng": 30.73348
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Героев Сталинграда, 98 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.644598,
 "lng": 32.559749
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, ул. Димитрова, 14",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 45.683463,
 "lng": 28.612357
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Болград, ул. Инзовская, 128",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.622259,
 "lng": 31.103819
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Южный, пр. Ленина, 19-З",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.494805,
 "lng": 30.19161
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Беляевка, ул. Ленина, 404",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.430267,
 "lng": 30.711806
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Генерала Петрова, 14",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.609536,
 "lng": 22.297933
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ужгород, ул. Станционная, 2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.617442,
 "lng": 22.296158
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ужгород, ул. Швабская, 21",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.450136,
 "lng": 35.001127
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Рабочая, 152",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.437986,
 "lng": 30.748333
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Черняховского, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.572776,
 "lng": 30.792838
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Днепропетровская дорога, 86",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 45.349355,
 "lng": 28.83552
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Измаил, пр. Суворова, 72",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.296221,
 "lng": 30.644727
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ильичевск, ул. Героев Сталинграда, 7",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.484475,
 "lng": 34.921546
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Кондратюка, 4",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.4281,
 "lng": 35.010056
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Новокрымская, 3 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.743019,
 "lng": 25.35792
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Луцк, ул. Ровенская, 1 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.872371,
 "lng": 35.051647
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Дудыкина, 28",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.948974,
 "lng": 33.452848
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Лисового, 14 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.880813,
 "lng": 33.369108
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, ул. Тбилисская, 2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.001454,
 "lng": 33.47687
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, м-н 4-й Заречный, 20 В",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.584399,
 "lng": 30.790617
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Добровольского, 106",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.479553,
 "lng": 30.749397
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пер. Сабанский, 2/4",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.467763,
 "lng": 30.748707
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, бул. Итальянский, 8",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.641146,
 "lng": 32.61305
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, пр. Ушакова, 49",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.860672,
 "lng": 35.101999
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, пр. Соборный, 226",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.422911,
 "lng": 30.71221
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Варненская, 16/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.475706,
 "lng": 30.731452
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Преображенская, 67",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.476265,
 "lng": 30.739438
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Ришельевская, 38",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.461932,
 "lng": 34.969366
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, ул. Мазепы, 58",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.950201,
 "lng": 33.443837
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кривой Рог, м-н Солнечный, 60/2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.928073,
 "lng": 24.712497
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Ивано-Франковск, ул. Военных ветеранов, 12",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 55.734391,
 "lng": 37.586214
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Академика Подстригача, 2",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.442825,
 "lng": 22.717798
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Мукачево, ул. Космонавта Беляева, 12",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.311781,
 "lng": 23.041894
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Иршава, ул. Белецкая, 20",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.84263,
 "lng": 23.971044
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Низинная, 2",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.807939,
 "lng": 24.055279
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Луганская, 6",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.231702,
 "lng": 28.455573
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Винница, ул. Пирогова, 6",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.521832,
 "lng": 25.046755
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Коломыя, ул. Винниченко, 1 Б",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.837747,
 "lng": 24.035441
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Ивана Франка, 3",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.813146,
 "lng": 23.974927
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Щирецкая, 36",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.834619,
 "lng": 24.006814
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Степана Бандеры, 71",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.81979,
 "lng": 23.980698
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Симона Петлюры, 37 А",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.84185,
 "lng": 24.001724
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Стороженко, 12",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.6212,
 "lng": 24.575968
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Надворная, ул. Соборная, 163",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.552419,
 "lng": 25.59125
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Тернополь, ул. Иосифа Слепого, 1",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.833198,
 "lng": 24.037833
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, пл. Петрушевича, 3",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.809814,
 "lng": 24.002327
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Владимира Великого, 51",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.839683,
 "lng": 24.029717
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, пр. Красной Калины, 36",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.624251,
 "lng": 22.303157
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Ужгород, ул. Фединца 40",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.423281,
 "lng": 26.994463
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Хмельницкий, ул. Шевченко, 11",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.481149,
 "lng": 30.727757
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Одесса, ул. Новосельского, 79",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.624926,
 "lng": 26.248653
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Ровно, пр. Мира, 12",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.745842,
 "lng": 25.334279
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Луцк, пр. Воли, 14",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.255962,
 "lng": 23.848381
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Стрый, ул. Коновальца, 3",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.25,
 "lng": 32.6
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Ичня, ул. Ленина, 19",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.836344,
 "lng": 24.027
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Львов, ул. Стефаныка, 15",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.840488,
 "lng": 35.128412
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Запорожье, ул. Лермонтова, 9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.550205,
 "lng": 25.588807
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Тернополь, ул. Русская, 14",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.39212,
 "lng": 30.371562
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Вишневое, ул. Октябрьская, 13",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.366394,
 "lng": 29.658381
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Тетиев, ул. Ленина, 29",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.865992,
 "lng": 30.822432
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кагарлык, ул. Карла Маркса, 3",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.359516,
 "lng": 30.937936
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Борисполь, ул. Киевский шлях, 41",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.796798,
 "lng": 30.131085
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Белая Церковь, бул. 50-летия Победы, 105",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.506294,
 "lng": 30.826651
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Бровары, ул. Красовского, 16",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.153128,
 "lng": 30.740462
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Украинка, ул. Юности, 6 Д",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.513538,
 "lng": 30.787495
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Бровары, ул. Гагарина, 9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.289303,
 "lng": 25.934079
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Черновцы, ул. Головна, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.615621,
 "lng": 26.26459
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ровно, ул. Княгини Ольги, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.225312,
 "lng": 28.446911
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Пирогова, 51",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.936617,
 "lng": 32.035647
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Николаев, ул. Космонавтов, 43",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.179929,
 "lng": 30.312824
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Васильков, ул. Грушевского, 12",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.918587,
 "lng": 24.71056
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ивано-Франковск, ул. Сечевых Стрельцов, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.058876,
 "lng": 23.973647
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Жовква, пл. Вечевая, 3",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.759672,
 "lng": 33.358113
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Каховка, ул. Ленина, 20",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.595075,
 "lng": 34.545518
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Полтава, пл. Независимости, 20",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.569309,
 "lng": 34.390333
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Никополь, пр. Трубников, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.373258,
 "lng": 35.448841
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Красноград, ул. Харьковская, 123",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.910483,
 "lng": 33.391783
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. 23-го февраля, 164",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.941539,
 "lng": 34.776805
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, ул. Курская, 115",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.292079,
 "lng": 25.935837
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Черновцы, ул. Русская, 253",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.231322,
 "lng": 28.518594
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, Немировское шоссе, 26",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.226128,
 "lng": 28.41258
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, пр. Юности, 43 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.421518,
 "lng": 26.98125
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Хмельницкий, ул. Театральная, 10",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.227888,
 "lng": 28.446296
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Пирогова, 56",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.235611,
 "lng": 28.463556
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Театральная, 10",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.225382,
 "lng": 28.424734
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Келецкая, 60",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.107833,
 "lng": 28.682026
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Вороновица, ул. Гагарина, 24",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.235464,
 "lng": 28.414244
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, Хмельницкое шоссе, 92",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.515919,
 "lng": 37.684448
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Константиновка, пр. Ломоносова, 127",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.079586,
 "lng": 29.912201
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Фастов, ул. Соборная, 34",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.160831,
 "lng": 37.485843
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Мариуполь, пр. Ленина, 81",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.230779,
 "lng": 28.461173
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Гоголя, 30",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.3639,
 "lng": 30.921268
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Борисполь, ул. Киевский шлях, 2/6",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.018413,
 "lng": 33.46492
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Симбирцева, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.909733,
 "lng": 33.3959
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Есенина, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.26024,
 "lng": 25.932883
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Первомайский, ул. Комарова, 26",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.458837,
 "lng": 35.044378
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Днепропетровск, ул. Артема, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.742487,
 "lng": 25.320146
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Луцк, ул. Леси Украинки, 24",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.429533,
 "lng": 35.039079
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Днепропетровск, пр. Гагарина, 74",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.451053,
 "lng": 30.76054
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Одесса, бул. Французский, 36",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.000078,
 "lng": 33.478506
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, м-н 4-й Заречный",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.882816,
 "lng": 33.383205
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Орджоникидзе, 18/18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.146479,
 "lng": 35.870965
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сахновщина, ул. Первого Мая, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.442417,
 "lng": 22.717338
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Мукачево, ул. Валенберга, 3",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.008251,
 "lng": 36.318727
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Академика Павлова, 120",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.366394,
 "lng": 29.658381
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Тетиев, ул. Ленина, 20",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.90957,
 "lng": 34.798096
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, ул. Воскресенская, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.52034,
 "lng": 30.806888
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Бровары, бул. Независимости, 16",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.973783,
 "lng": 36.257737
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Гагарина, 43",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.230378,
 "lng": 28.534191
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Чехова, 7 В",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.854428,
 "lng": 35.345687
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Мелитополь, ул. Зиндельса, 23",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.350705,
 "lng": 31.318891
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Барышевка, ул. Октябрьская, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.069234,
 "lng": 33.420901
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кременчуг, ул. Халаменюка, 4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.438762,
 "lng": 30.751205
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Одесса, ул. Черняховского, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.968536,
 "lng": 31.971315
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Николаев, пр. Ленина, 22",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.905239,
 "lng": 33.377174
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, пр. Мира, 7 Б",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.512867,
 "lng": 32.26563
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кировоград, ул. Шевченко, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.505186,
 "lng": 32.234536
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кировоград, ул. Академика Королева, 25 Б",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.911401,
 "lng": 34.825786
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, пр. Михаила Лушпы, 22",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.964521,
 "lng": 33.437377
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, пр. 200-летия Кривого Рога, 7 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.918587,
 "lng": 24.71056
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ивано-Франковск, ул. Сечевых Стрельцов, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.253517,
 "lng": 28.663807
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Житомир, ул. Большая Бердичевская, 10",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.746261,
 "lng": 25.33469
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Луцк, пр. Воли, 21",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.929874,
 "lng": 35.203865
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Запорожье, ул. Ленина, 83",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.621562,
 "lng": 22.296394
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ужгород, Киевская набережная, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.992855,
 "lng": 33.438148
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Кремлевская, 28",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.036045,
 "lng": 33.47994
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Мусоргского, 22",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.531992,
 "lng": 35.86733
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Павлоград, ул. Ленина, 105",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.164365,
 "lng": 35.540944
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Лозовая, ул. Карла Либкнехта, 15",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.855022,
 "lng": 35.3587
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Мелитополь, пр. Богдана Хмельницкого, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.173463,
 "lng": 23.297248
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Хуст, ул. Богдана Хмельницкого, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.915017,
 "lng": 24.70208
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ивано-Франковск, ул. Шевченко, 57",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.240313,
 "lng": 28.506161
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Папанина, 1 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.507933,
 "lng": 32.262317
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кировоград, ул. Октябрьской революции, 20",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.513912,
 "lng": 32.262981
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кировоград, ул. Шевченко, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.50644,
 "lng": 32.2658
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кировоград, ул. Преображенская, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.481064,
 "lng": 34.965436
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Тростянец, ул. Ленина, 42",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.939298,
 "lng": 24.685575
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ивано-Франковск, ул. Федьковича, 91",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.86426,
 "lng": 24.016439
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Львов, пр. Черновола, 99",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.663619,
 "lng": 25.778394
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Збараж, майдан И. Франка, 40",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.813146,
 "lng": 23.974927
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Львов, ул. Щирецкая, 36",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.976066,
 "lng": 31.992027
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Николаев, ул. Адмиральская, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.152458,
 "lng": 30.744123
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Украинка, пр. Днепровский, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.825685,
 "lng": 31.17124
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Южноукраинск, пр. Ленина, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.477274,
 "lng": 30.741449
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Одесса, ул. Пушкинская, 32",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.128622,
 "lng": 30.656428
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Обухов, ул. Киевская, 158",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.915169,
 "lng": 34.79993
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, ул. Горького, 5 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.583173,
 "lng": 34.537523
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Полтава, ул. Сенная, 2/39",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.468973,
 "lng": 29.813007
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Макаров, ул. Фрунзе, 34",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.583343,
 "lng": 34.558253
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Полтава, ул. Гагарина, 3",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.620332,
 "lng": 26.24275
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ровно, ул. Соборная, 260",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.618838,
 "lng": 26.248702
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ровно, ул. Короленко, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.899202,
 "lng": 34.819383
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, ул. Харьковская, 38",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.089913,
 "lng": 36.144259
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Дергачи, ул. Железнодорожная, 31",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.913162,
 "lng": 34.796253
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Сумы, ул. Засумская, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.317271,
 "lng": 28.799293
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Овруч, ул. Советская, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.001976,
 "lng": 36.245725
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Пушкинская, 68",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.964369,
 "lng": 36.320846
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Маршала Жукова, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.835348,
 "lng": 36.686513
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Чугуев, ул. Харьковская, 111",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.000381,
 "lng": 36.235324
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Сумская, 40",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.001976,
 "lng": 36.245725
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Пушкинская, 68",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 44.592721,
 "lng": 33.551543
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Дергачи, пл.  Победы, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.840453,
 "lng": 36.686866
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Чугуев, ул. Харьковская, 105 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.966344,
 "lng": 36.323419
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Московский, 257",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.039644,
 "lng": 36.221682
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Науки, 56 ",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.109448,
 "lng": 36.123184
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Дергачи, ул. Петровского, 163 Г",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.293894,
 "lng": 36.935884
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Волчанск, ул. Ленина, 68",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.009302,
 "lng": 36.240059
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Сумская, 100",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.031611,
 "lng": 36.221965
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Ленина, 56",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.910999,
 "lng": 36.425952
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Роганская, 151",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.022836,
 "lng": 36.337007
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Героев Труда, 26",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.447834,
 "lng": 36.838255
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Балаклея, ул. Октябрьская, 39",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.025729,
 "lng": 36.221196
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Ленина, 27 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.639938,
 "lng": 32.609411
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Херсон, ул. Маяковского, 16 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.421808,
 "lng": 26.988628
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Хмельницкий, ул. Проскуровская, 50",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.752401,
 "lng": 30.218589
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Умань, ул. Ленина, 9/2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.444386,
 "lng": 32.061394
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Черкассы, ул. Лазарева, 4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.491766,
 "lng": 31.292317
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Чернигов, пр. Победы, 75",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.433603,
 "lng": 32.077219
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Черкассы, бул. Шевченко, 320",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.950599,
 "lng": 36.260875
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Гагарина, 167/1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.890236,
 "lng": 36.308001
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Лозовая, 2-й микрорайон, 16 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.253599,
 "lng": 35.708443
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Токмак, ул. Революционная, 49",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.8384749,
 "lng": 35.2955242
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Коломак, ул. Победы, 123",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.256819,
 "lng": 31.781765
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Яготин, ул. Независимости, 104",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.81943,
 "lng": 35.047818
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, ул. Гудыменко, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.773386,
 "lng": 24.01079
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сокольники, ул. Стрыйская, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.457626,
 "lng": 35.120007
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Карловка, ул. Первомайская, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.478371,
 "lng": 36.253201
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Пологи, ул. Горького, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.392023,
 "lng": 33.259997
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Глобино, ул. Октябрьская, 13",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.026557,
 "lng": 36.219337
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Отакара Яроша, 18 Д ",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.960319,
 "lng": 36.320966
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, Стадионный проезд, 5",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.5631405,
 "lng": 32.2123092
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Крутьки, ул. Устименко, 104",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.459633,
 "lng": 35.04927
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, ул. Южная, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.44231,
 "lng": 30.714509
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, ул. Малиновского, 51",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.943364,
 "lng": 38.475226
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Северодонецк, пр. Химиков, 38/19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.496333,
 "lng": 35.11797
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, ул. Курсантская, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.730642,
 "lng": 29.6601666
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сквира, ул. Карла Либкнехта, 27",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.839683,
 "lng": 24.029717
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, пр. Красной Калины, 109",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.121739,
 "lng": 30.646821
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Обухов, ул. Киевская, 130",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.228291,
 "lng": 28.398331
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Келецкая, 122 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.243892,
 "lng": 28.485308
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Фрунзе, 59",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.030444,
 "lng": 24.359928
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Калуш, пр. Леси Украинки, 4 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.89988,
 "lng": 33.393364
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кривой Рог, пр. Металлургов, 9",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.3053444,
 "lng": 34.4689203
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Комыши, ул. Киевская, 65",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.627373,
 "lng": 27.894854
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ждановка, ул. Заводская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.9975747,
 "lng": 24.19831
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Брошнив-Осада, ул. 22-го Января, 94",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.076622,
 "lng": 33.416878
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кременчуг, ул. 40 лет Октября, 14/69",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.584778,
 "lng": 34.54624
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Полтава, ул. Шевченко, 52",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.982433,
 "lng": 36.17971
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Полтавский шлях, 148/2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.838108,
 "lng": 24.040778
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Пекарская, 23",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.986545,
 "lng": 36.228408
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Павловская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.812253,
 "lng": 23.977449
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Выговского, 100",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.822015,
 "lng": 35.171226
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, пр. Соборный, 92",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.121739,
 "lng": 30.646821
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Обухов, ул. Киевская, 130",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.836942,
 "lng": 24.032033
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, пр. Шевченко, 15",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.835005,
 "lng": 23.997577
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Городоцкая, 167",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.388305,
 "lng": 30.174683
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ставище, ул. Цимбала, 57",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.836839,
 "lng": 24.04258
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Пекарская, 50",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 54.03036,
 "lng": 38.31518
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новомосковск, ул. Победы, 8",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.23431,
 "lng": 28.464509
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Театральная, 15",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.131707,
 "lng": 26.297675
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Калиновка, ул. Шевченко, 33",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.165449,
 "lng": 31.76222
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Зоря, ул. Промышленная, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.128166,
 "lng": 33.402671
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кременчуг, ул. Ленина, 14/23",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.078807,
 "lng": 25.147894
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Броды, ул. Рынок, 30/31",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.529921,
 "lng": 35.870391
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Павлоград, ул. Шевченко, 118",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.754322,
 "lng": 25.332772
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Луцк, пр. Грушевского, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.439843,
 "lng": 30.745522
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, Фонтанская дорога, 25 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.966255,
 "lng": 31.992805
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Николаев, пр. Ленина, 83 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.009303,
 "lng": 36.352378
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Валентиновская, 38 В",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.914579,
 "lng": 34.800181
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сумы, ул. Горького, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.07156,
 "lng": 31.460877
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Переяслав-Хмельницкий, ул. Богдана Хмельницкого, 61",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.9935,
 "lng": 36.230383
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Конарева, 12",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.610973,
 "lng": 26.275323
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ровно, ул. Степана Бандеры, 60 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.317224,
 "lng": 29.054143
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Коростышев, ул. Киевская, 103",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.443569,
 "lng": 34.988836
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, пр. Правды, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 52.98528,
 "lng": 78.623712
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Славгород, ул. Заводская, 1 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.620551,
 "lng": 22.292178
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ужгород, ул. Льва Толстого, 29",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.027227,
 "lng": 36.22582
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Отакара Яроша, 24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.705557,
 "lng": 37.6028
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Купянск, ул. Сватовская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.9641116,
 "lng": 36.3440023
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Коломийцы, ул. Ленина, 36",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.663381,
 "lng": 32.627877
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Херсон, Бериславское шоссе, 37",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.570666,
 "lng": 34.378227
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Никополь, пр. Трубников, 23",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.1086169,
 "lng": 24.3383275
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Камянка-Бусская, ул. Ярослава Мудрого, 62",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.9810718,
 "lng": 36.2324087
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Покровское, ул. 40-летия Октября, 5 Ж",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.350882,
 "lng": 23.506697
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Дрогобыч, пл. Рынок, 20",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.217391,
 "lng": 28.437823
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Пирогова, 109",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.919933,
 "lng": 34.798316
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сумы, ул. Горького, 25",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.219154,
 "lng": 32.525996
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Пирятин, ул. Сумская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.596506,
 "lng": 36.524956
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Слобожанское, ул. Циолковского, 20",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.587365,
 "lng": 30.803156
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, Днепропетровская дорога, 126/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.922066,
 "lng": 24.724796
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ивано-Франковск, ул. Железнодорожная, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.5545035,
 "lng": 28.5098403
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Томашполь, ул. Криворучко, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.365292,
 "lng": 33.540642
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чаплынка, ул. Советская, 2 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.745551,
 "lng": 25.402946
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Струмовка, ул. Ровенская, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.515779,
 "lng": 34.606096
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепродзержинск, ул. Медицинская, 1/11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.457549,
 "lng": 34.264905
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Федоровка, ул. Ленина, 12",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.6719742,
 "lng": 32.3212702
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чернобай, ул. Ценральная, 96/27",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.67968,
 "lng": 26.588338
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Каменец-Подольский, ул. Соборная, 27",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.458239,
 "lng": 35.135967
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Карловка, ул. Спартака, 3 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.6034734,
 "lng": 29.9470714
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Пилиповичи, ул. Привокзальная, 15",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.038283,
 "lng": 23.514092
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сколе, майдан Независимости, 1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.973783,
 "lng": 36.257737
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, пр. Гагарина, 43",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.694406,
 "lng": 36.359548
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Змиев, ул. 50 лет Комсомола, 61",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.624636,
 "lng": 34.518888
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Червоногригоровка, ул. Кооперативная, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.070061,
 "lng": 33.422267
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кременчуг, ул. Халаменюка, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.6190537,
 "lng": 34.6483889
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Елизаветовка, ул. Б. Хмельницкого, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.749902,
 "lng": 31.464155
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Канев, ул. Ленина, 161/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.3639,
 "lng": 30.921268
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Борисполь, ул. Киевский шлях, 2/6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.622649,
 "lng": 31.10274
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Южное, пр. Мира, 13/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.530492,
 "lng": 25.041205
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Коломыя, пл. Возрождения, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.988404,
 "lng": 36.230539
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, ул. Университетская, 27",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.97898,
 "lng": 33.598178
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Миргород, ул. Гоголя, 154",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.472166,
 "lng": 35.022184
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, ул. Шмидта, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.304794,
 "lng": 34.897703
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ахтырка, ул. Батюка, 26",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.350477,
 "lng": 30.953696
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Борисполь, ул. Киевский шлях, 75",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.218834,
 "lng": 28.437354
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Пирогова, 112",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.350705,
 "lng": 31.318891
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Барышевка, ул. Октябрьская, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.506224,
 "lng": 32.269695
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кировоград, ул. Гоголя, 91/46",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.193849,
 "lng": 30.337862
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белгород-Днестровский, ул. Московская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.756959,
 "lng": 33.367045
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новая Каховка, ул. Первомайская, 19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.822622,
 "lng": 23.973282
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Любинская, 100",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.821879,
 "lng": 31.179564
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Южноукраинск, ул. Ленина, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.215589,
 "lng": 24.704404
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ковель, ул. Независимости, 138",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.812338,
 "lng": 35.182394
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, пр. Соборный, 50/24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.235611,
 "lng": 28.463556
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Театральная, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.926095,
 "lng": 24.722735
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ивано-Франковск, ул. Привокзальная, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.192999,
 "lng": 30.352606
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белгород-Днестровский, ул. Кирова, 31",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.783653,
 "lng": 33.252664
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Хорол, ул. Небесной сотни, 42",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.282432,
 "lng": 25.936492
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Черновцы, ул. Первомайская, 19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.821721,
 "lng": 30.129446
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белая Церковь, ул. Сухоярская, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.421518,
 "lng": 26.98125
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Хмельницкий, ул. Театральная, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.837911,
 "lng": 36.69001
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чугуев, бул. Комарова, 12",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.233822,
 "lng": 28.466502
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Соборная, 68",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.005002,
 "lng": 36.235029
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, пл. Свободы, 8",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.240943,
 "lng": 33.205052
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Конотоп, пр. Красной Калины, 8",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.7034814,
 "lng": 31.2981113
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Степанци, ул. Полевая, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.54579,
 "lng": 27.931784
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Хмельник, ул. 1-го Мая, 24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.630899,
 "lng": 32.611646
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Херсон, ул. Октябрьской революции, 19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.677811,
 "lng": 33.911362
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Глухов, ул. Киево-Московская, 30 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.589645,
 "lng": 27.613802
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новоград-Волынский, ул. Шевченко, 28/2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.358872,
 "lng": 33.259035
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Лохвица, ул. Победы, 13",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.592578,
 "lng": 34.379116
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Никополь, пр. Электрометаллургов, 302",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.858913,
 "lng": 35.103326
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, пр. Соборный, 222",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.66855,
 "lng": 33.109211
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Александрия, пр. Ленина, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.244235,
 "lng": 32.51344
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Пирятин, ул. Ленина, 32",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.637689,
 "lng": 24.294862
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Бобрка, ул. Тарнавского, 22",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.435695,
 "lng": 32.071545
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Черкассы, ул. Богдана Хмельницкого, 52",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.741509,
 "lng": 33.480953
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ромны, ул. Карла Маркса, 86",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.861478,
 "lng": 24.051312
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Богдана Хмельницкого, 176",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.751001,
 "lng": 30.219234
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Умань, ул. Ленина, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.893534,
 "lng": 35.145844
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, ул. Лизы Чайкиной, 51",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.959525,
 "lng": 36.113268
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Солоницевка, ул. Заводская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.949691,
 "lng": 29.457087
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Попельня, ул. Богдана Хмельницкого, 9",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.665636,
 "lng": 36.25356
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Гуляйполе, ул. Петровского, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4791941,
 "lng": 24.2790651
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сокаль, ул. Тартаковская, 7",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.395718,
 "lng": 24.230498
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Червоноград, ул. Сокальская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.958042,
 "lng": 33.639362
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Миргород, ул. Минзаводская, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.848195,
 "lng": 24.325657
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Владимир-Волынский, ул. Ковельская, 73",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.424845,
 "lng": 35.026674
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, пр. Гагарина, 171",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.953214,
 "lng": 28.645754
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Коростень, ул. Красина, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.821241,
 "lng": 35.023725
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, ул. Сапожникова, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.290276,
 "lng": 36.937739
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Волчанск, ул. Ленина, 96",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 59.027926,
 "lng": 52.35211
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Песковка, ул. Октябрьская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.538953,
 "lng": 35.867924
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Павлоград, ул. Карла Маркса, 41",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.494413,
 "lng": 31.297759
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чернигов, ул. Пятницкая, 16",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.204632,
 "lng": 34.363853
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Зеньков, ул. Ленина, 38",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.239538,
 "lng": 28.499343
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, пр. Коцюбинского, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.250999,
 "lng": 28.656305
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Житомир, ул. Леха Качинского",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.301136,
 "lng": 30.654404
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Черноморск, ул. 1-го Мая, 5 В",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.551113,
 "lng": 25.566506
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тернополь, пл. Победы, 4 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.47689,
 "lng": 30.73197
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, ул. Преображенская, 66",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.583717,
 "lng": 34.392574
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Никополь, ул. Шевченко, 243",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.720843,
 "lng": 35.16908
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чутово, ул. Октябрьская, 108 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.594783,
 "lng": 34.541631
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Полтава, ул. Октябрьская, 50",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.231466,
 "lng": 28.456962
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Пирогова, 9",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.918777,
 "lng": 24.71018
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ивано-Франковск, ул. Сечевых Стрельцов, 42 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.79653,
 "lng": 30.117643
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белая Церковь, ул. Ярослава Мудрого, 17",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.04511,
 "lng": 30.847221
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Первомайск, ул. Грушевского, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.926075,
 "lng": 24.710226
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ивано-Франковск, ул. Галицкая, 22",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.779951,
 "lng": 35.214783
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, ул. Чумаченко, 34",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.48349,
 "lng": 30.741609
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, ул. Дерибасовская, 9",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.904714,
 "lng": 34.819568
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Сумы, пр. Михаила Лушпы, 4/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.565069,
 "lng": 34.079701
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Решетиловка, ул. Октябрьская, 8",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.228615,
 "lng": 28.42532
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. 600-летия, 36",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.322551,
 "lng": 35.503233
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Синельниково, ул. Мира, 26 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.669214,
 "lng": 24.559317
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Перемышляны, ул. Привокзальная, 1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.017152,
 "lng": 23.572467
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тячев, ул. Ленина, 16",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.442827,
 "lng": 22.72049
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Мукачево, ул. Новый Пассаж, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 56.030045,
 "lng": 45.053593
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чернухи, ул. Ленина, 32",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.343115,
 "lng": 34.314481
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новые Санжары, ул. Октябрьская, 19/29",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.865095,
 "lng": 30.823619
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кагарлык, ул. Независимости, 5",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.568614,
 "lng": 34.463395
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Лебедин, ул. Героев Майдана, 12",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.906615,
 "lng": 38.44336
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Лисичанск, ул. Чекистов, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.811263,
 "lng": 29.378338
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Гайсин, ул. Октябрьская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.783974,
 "lng": 23.642388
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Городок, ул. Перемышльская, 16 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.966037,
 "lng": 33.60861
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Миргород, ул. Гоголя, 139 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.068824,
 "lng": 34.764534
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Котельва, ул. Октябрьская, 214",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.225893,
 "lng": 28.436047
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, ул. Келецкая, 36",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.299615,
 "lng": 32.350668
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Худяки, ул. Кирова, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.725806,
 "lng": 24.162834
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Нововолынск, бул. Шевченка, 8",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.592173,
 "lng": 37.99982
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Бахмут, ул. Мира, 42",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.863269,
 "lng": 24.016726
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, пр. Черновола, 95",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.8339,
 "lng": 24.034597
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Ивана Франка, 35",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.585242,
 "lng": 34.557969
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Полтава, ул. Гоголя, 19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.322904,
 "lng": 35.521396
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Синельниково, ул. 50-летия Октября, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.1022204,
 "lng": 24.3444208
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Камянка-Бусская, ул. Независимости, 32",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.715484,
 "lng": 23.905562
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Пустомыты, ул. Грушевского, 66",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.855022,
 "lng": 35.3587
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Мелитополь, пр. Богдана Хмельницкого, 22",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.2791336,
 "lng": 24.6455255
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Радехов, ул. Лопатинская, 2 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.180837,
 "lng": 30.309219
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Васильков, ул. Грушевского, 31",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.890236,
 "lng": 36.308001
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Лозовая, ул. Михаила Грушевского, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.505963,
 "lng": 32.261333
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кропивницкий, ул. Набережная, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.350705,
 "lng": 31.318891
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Барышевка, ул. Комсомольская, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.239489,
 "lng": 28.509192
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, пл. Героев Сталинграда (остановка)",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.848553,
 "lng": 24.016052
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Клепаровская, 18",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.328126,
 "lng": 31.499663
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Березань, пл. Привокзальная, 1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.553517,
 "lng": 25.594767
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Тернополь, ул. Листопадная, 7",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.9935,
 "lng": 36.230383
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. 50-летия ВЛКСМ, 56",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.847745,
 "lng": 35.111751
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, бул. Шевченко, 18",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.206234,
 "lng": 22.642341
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Берегово, ул. Кошута, 7",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.512935,
 "lng": 30.792955
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Бровары, бул. Независимости, 3",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.839981,
 "lng": 35.120717
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, ул. Победы, 59",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.997127,
 "lng": 36.236339
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, ул. Чернышевского, 7/9",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.516434,
 "lng": 34.614225
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепродзержинск, пр. Ленина, 49",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.75949,
 "lng": 36.790298
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Бердянск, пр. Ленина, 12/22",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.740115,
 "lng": 37.584839
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Краматорск, ул. Шкадинова, 42",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.01819,
 "lng": 36.22284
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Ленина, 17",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.906648,
 "lng": 34.798021
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Сумы, ул. Красная площадь, 5",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, пр. Ленина, 144",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.422796,
 "lng": 32.051401
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Черкассы, ул. Громова, 2",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, пр. Ленина, 66",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.835081,
 "lng": 24.034771
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, ул. Ивана Франка, 20",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.241477,
 "lng": 28.479112
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Винница, ул. Киевская, 38 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.380681,
 "lng": 27.343744
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Голосков, ул. Центральная, 1/1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.621443,
 "lng": 22.296345
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Ужгород, Киевская набережная, 3",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.585826,
 "lng": 34.549538
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Полтава, ул. Пушкина, 28",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.486183,
 "lng": 30.742744
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, бул. Приморский, 14",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.481131,
 "lng": 30.745273
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, ул. Бунина, 10",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.967313,
 "lng": 32.004339
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Николаев, ул. Садовая, 10 ",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.465854,
 "lng": 35.046043
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Центральная, 12",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.458658,
 "lng": 35.04413
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Артема, 20",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.25267,
 "lng": 28.657299
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Житомир, ул. Черняховского, 8",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.853583,
 "lng": 36.323213
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Васищево, ул. Промышленная, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.271553,
 "lng": 23.788577
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Нежухов, ул. Леоны, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.822054,
 "lng": 35.196348
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, пр. Моторостроителей, 15 ",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.271553,
 "lng": 23.788577
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Нежухов, ул. Леоны, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.271553,
 "lng": 23.788577
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Нежухов, ул. Леоны, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.837911,
 "lng": 24.008389
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, ул. Шептицких, 26",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.435834,
 "lng": 30.748492
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, ул. Тополева, 10 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.973759,
 "lng": 36.255586
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Гагарина, 66-68",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.985593,
 "lng": 36.189933
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, ул. Полтавский шлях, 126",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.512388,
 "lng": 32.263851
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Кировоград, ул. Декабристов, 6",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.128166,
 "lng": 33.402671
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Кременчуг, ул. Ленина, 26/37",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.793546,
 "lng": 30.11635
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Белая Церковь, ул. Гагарина, 11",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.443498,
 "lng": 34.99789
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Рабочая, 168",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 45.339036,
 "lng": 28.833508
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Измаил, пр. Суворова, 25",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.620118,
 "lng": 26.272238
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Ровно, ул. Грушевского, 42 Б",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.530032,
 "lng": 35.866964
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Павлоград, ул. Шевченко, 128",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.953427,
 "lng": 32.040487
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Николаев, пр. Мира, 4/5",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.259003,
 "lng": 23.852273
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Стрый, ул. Шевченко, 87",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.921333,
 "lng": 24.705155
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Ивано-Франковск, ул. П. Орлика, 8",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.629207,
 "lng": 32.606393
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Херсон, ул. Ленина, 23",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.910028,
 "lng": 33.399165
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Кривой Рог, пр. Гагарина, 25 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.437224,
 "lng": 26.983036
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Хмельницкий, ул. Нижняя береговая, 35",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.23269,
 "lng": 28.457946
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Винница, ул. Гоголя, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.017152,
 "lng": 23.572467
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Тячев, ул. Ленина, 53",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.51041,
 "lng": 35.085708
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Гули Королевой, 1 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.857034,
 "lng": 24.020096
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, пр. Черновола, 59",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.855022,
 "lng": 35.3587
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Мелитополь, пр. Богдана Хмельницкого, 39",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.966871,
 "lng": 31.983129
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Николаев, пр. Ленина, 67",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.744869,
 "lng": 25.322631
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Луцк, ул. Леси Украинки, 53",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.467827,
 "lng": 35.056745
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Рогалёва, 33",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.98772,
 "lng": 36.253448
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, ул. Богдана Хмельницкого, 24 Б",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.482526,
 "lng": 30.72331
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, ул. Белинского, 8",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.681592,
 "lng": 26.590885
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Каменец-Подольский, ул. Данилы Галицкого, 13",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.042675,
 "lng": 30.850752
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Первомайск, ул. Шевченко, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.495873,
 "lng": 31.306132
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Чернигов, ул. Гетьмана Полуботка, 18",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.291254,
 "lng": 25.936677
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Черновцы, ул. Доброго, 7",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.425653,
 "lng": 30.717353
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, ул. Варненская, 11",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.434597,
 "lng": 30.73348
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Одесса, ул. Героев Сталинграда, 62",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.955767,
 "lng": 36.363521
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Московский, 262",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 53.412445,
 "lng": 58.97181
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, ул. Научная, 96 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.468254,
 "lng": 22.647072
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Мукачево, пл. Мира, 18/2",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.479432,
 "lng": 30.736512
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Жуковского, 33",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.296779,
 "lng": 30.65261
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Ильичевск, ул. Ленина, 28 Б",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.47355,
 "lng": 30.739386
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Ришельевская, 55",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.455333,
 "lng": 30.752317
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, пр. Шевченко, 11 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.950498,
 "lng": 36.260918
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, пр. Гагарина, 167",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.006866,
 "lng": 36.237087
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Сумская, 59",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.034977,
 "lng": 36.21986
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, пр. Ленина, 41-43",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.988823,
 "lng": 36.233709
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, пер. Армянский, 1/3",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.79877,
 "lng": 30.122119
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Белая Церковь, ул. Ярослава Мудрого, 42",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.987385,
 "lng": 36.21686
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Полтавский шлях, 31",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.809583,
 "lng": 24.005095
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Львов, ул. Владимира Великого, 35 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.841774,
 "lng": 24.022272
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Львов, пл. Генерала Григоренко, 4",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.838374,
 "lng": 24.032598
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Львов, ул. Князя Романа, 18",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.529921,
 "lng": 35.870391
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Павлоград, ул. Шевченко, 118 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Запорожье, пр. Ленина, 46",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.44309,
 "lng": 32.057313
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Черкассы, ул. Байды Вишневецкого, 47",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.442899,
 "lng": 35.017713
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, пр. Кирова, 115",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.473041,
 "lng": 35.026641
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, пр. Карла Маркса, 105",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Запорожье, пр. Ленина, 172",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.461215,
 "lng": 35.054214
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, пр. Карла Маркса, 34 Б",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Запорожье, пр. Ленина, 146",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.97314,
 "lng": 31.993732
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Николаев, ул. Спасская, 50/4",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.587928,
 "lng": 34.555255
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Полтава, ул. Октябрьская, 32",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.746841,
 "lng": 25.328939
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Луцк, пр. Воли, 9",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.29042,
 "lng": 25.935189
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Черновцы, ул. Головна, 61/63",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.464507,
 "lng": 35.030182
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, пр. Пушкина, 19",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.847745,
 "lng": 35.111751
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Запорожье, бул. Шевченко, 18",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.520664,
 "lng": 34.616015
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Камянское, пр. Свободы, 35 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.909925,
 "lng": 33.391221
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Кривой Рог, ул. Волгоградская, 9",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.476981,
 "lng": 30.742316
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Пушкинская, 35",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.000631,
 "lng": 36.23497
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Сумская, 42",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.068229,
 "lng": 33.424987
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Кременчуг, ул. Халаменюка, 14",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.997511,
 "lng": 36.239673
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Пушкинская, 40",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.429643,
 "lng": 35.010669
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, ул. Титова, 11",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.259445,
 "lng": 25.952409
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Черновцы, ул. Энтузиастов, 3",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.909,
 "lng": 33.404935
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Кривой Рог, пр. Гагарина, 38",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.411971,
 "lng": 30.718971
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Королева, 18",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.42744,
 "lng": 35.035342
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, пр. Гагарина, 127",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.794512,
 "lng": 24.06067
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Львов, ул. Зубровская, 27",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.160831,
 "lng": 37.485843
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Мариуполь, пр. Ленина, 72",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.964607,
 "lng": 32.01638
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Николаев, пр. Ленина, 173",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.91021,
 "lng": 34.800287
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Сумы, ул. Соборная, 36",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.417768,
 "lng": 25.743343
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Дубно, ул. Даниила Галицкого, 1",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.255771,
 "lng": 28.664789
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Житомир, ул. Михайловская, 16",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.425228,
 "lng": 26.982184
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Хмельницкий, ул. Проскуровская, 16",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.903776,
 "lng": 33.342285
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Кривой Рог, пр. Карла Маркса, 20",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.575304,
 "lng": 30.796997
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Днепропетровская дорога, 93 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.839225,
 "lng": 35.137187
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, пр. Соборный, 135",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.839683,
 "lng": 24.029717
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Львов, ул. Госпитальная, 1",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.745359,
 "lng": 25.341859
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, пр. Воли, 33 А",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.259334,
 "lng": 28.662539
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Житомир, ул. Щорса, 18",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.743204,
 "lng": 25.357526
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, ул. Задворецкая, 2",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.75563,
 "lng": 25.357943
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, пр. Соборности, 43",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.284275,
 "lng": 25.938226
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Черновцы, ул. Головна, 111",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.608616,
 "lng": 22.267361
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Ужгород, ул. Легоцкого, 19 А",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.747233,
 "lng": 25.325383
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, ул. Гилака, 20",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.948242,
 "lng": 36.115992
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Харьков, ул. Красноармейская, 12",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.774848,
 "lng": 25.361102
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, ул. Конякина, 14",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.46106,
 "lng": 35.047988
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Днепропетровск, ул. Артема, 3 А",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.926674,
 "lng": 24.709299
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Ивано-Франковск, ул. Галицкая, 53 Б",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.898716,
 "lng": 36.113979
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Харьков, пр. Правды, 17",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.859829,
 "lng": 24.033622
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Заповитная, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.600956,
 "lng": 34.574715
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепродзержинск, ул. Строителей, 27 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.030444,
 "lng": 24.359928
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Калуш, пр. Леси Украинки, 1",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.922147,
 "lng": 24.708336
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Ивано-Франковск, ул. Галицкая, 7",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.275505,
 "lng": 37.178472
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Покровск, пр. Шахтостроителей, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.966344,
 "lng": 36.323419
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, пр. Московский, 257",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.8388,
 "lng": 35.139567
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, пр. 50-летия Октября, 21",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.529416,
 "lng": 35.030787
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Днепропетровск, ул. Нижнеднепровская, 17",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.452296,
 "lng": 30.753678
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Шевченко, 10/9",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.435352,
 "lng": 30.729792
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Краснова, 6/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.585732,
 "lng": 34.550425
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Полтава, ул. Фрунзе, 12",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.464507,
 "lng": 35.030182
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Днепропетровск, пр. Пушкина, 19",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.25867,
 "lng": 28.669863
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Житомир, ул. Киевская, 39",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.834131,
 "lng": 24.034854
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Львов, ул. Зеленая, 6",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.583198,
 "lng": 30.800313
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Одесса, ул. Генерала Бочарова, 53",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.435815,
 "lng": 30.726275
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Одесса, Люстдорфская дорога, 54",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.481632,
 "lng": 30.736691
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Одесса, пер. Красный, 11",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.13141,
 "lng": 30.656558
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Обухов, ул. Киевская, 119",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.432345,
 "lng": 35.125356
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, ул. Базовая, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 54.071469,
 "lng": 38.172449
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новомосковск, ул. Советская, 33/33",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.010991,
 "lng": 33.62774
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Комсомольск, ул. Ленина, 54",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.506668,
 "lng": 32.263316
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Кировоград, ул. Большая Перспективная, 50",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.653243,
 "lng": 32.606178
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Херсон, пр. Ушакова, 87",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.998605,
 "lng": 36.241741
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Харьков, ул. Дарвина, 1",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.481064,
 "lng": 34.965436
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тростянец, ул. Ленина, 39",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.986939,
 "lng": 36.207022
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Красноармейская",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.488203,
 "lng": 30.680435
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Ядова, 26",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.582841,
 "lng": 30.806356
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Бочарова, 59",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.473377,
 "lng": 30.737769
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Одесса, ул. Екатерининская, 75",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.619846,
 "lng": 26.242933
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Ровно, ул. Соборная, 65",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.957491,
 "lng": 32.041847
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Николаев, ул. Строителей, 5 Г",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Запорожье, пр. Ленина, 42",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.5964039,
 "lng": 33.862023
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Калининское, ул. Первомайская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.223588,
 "lng": 31.828238
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Смела, ул. Дзержинского, 4 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.583766,
 "lng": 30.808094
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Бочарова, 44",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.717597,
 "lng": 25.310286
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Луцк, бул. Дружбы Народов, 3",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.836321,
 "lng": 24.001217
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Львов, ул. Городоцкая, 151",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.644503,
 "lng": 29.91463
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Бородянка, ул. Центральная, 238",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.863452,
 "lng": 35.094917
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Запорожье, пр. Ленина, 66",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.236648,
 "lng": 28.486845
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Винница, пр. Коцюбинского, 78",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.963623,
 "lng": 31.988638
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Николаев, ул. Соборная, 40",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.281462,
 "lng": 31.155251
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Любарцы, ул. Ленина, 69 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.979665,
 "lng": 36.287088
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Харьков, пр. Московский, 195",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.95818,
 "lng": 36.392789
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Фрунзе, 3",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.95818,
 "lng": 36.392789
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Фрунзе, 3",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.95818,
 "lng": 36.392789
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пр. Фрунзе, 3",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.444481,
 "lng": 32.061574
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Черкассы, ул. Лазарева, 6",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.839964,
 "lng": 24.032833
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Львов, ул. Валова, 13",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.509319,
 "lng": 32.242742
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Кировоград, ул. Тореза, 27",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.485208,
 "lng": 30.746832
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пл. Таможенная, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.961534,
 "lng": 36.320016
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Харьков, бул. Юрьева, 1",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.578273,
 "lng": 34.576818
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Полтава, ул. Ленина, 69",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.841444,
 "lng": 24.02465
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Академика Гнатюка, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.606403,
 "lng": 22.28838
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Ужгород, ул. Минайская, 24",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.532612,
 "lng": 35.871449
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Павлоград, ул. Ленина, 91",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.502831,
 "lng": 30.326572
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Теплодар, ул. Пионерская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.238556,
 "lng": 36.987932
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Удачное, ул. Железнодорожная, 53",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.986689,
 "lng": 36.227313
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, пер. Банный, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.50827,
 "lng": 32.259973
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Кировоград, ул. Островского, 2",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.429447,
 "lng": 30.72752
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Академика Филатова, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.233528,
 "lng": 28.463963
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Винница, ул. Соборная, 81",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.466146,
 "lng": 30.736109
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Водопроводная, 1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.884195,
 "lng": 35.073034
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, ул. Бородинская, 7",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.852146,
 "lng": 35.115812
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Запорожье, пр. Соборный, 208",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.411396,
 "lng": 27.016582
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Хмельницкий, ул. Черновола, 24",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.558224,
 "lng": 32.900145
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Новая Прага, ул. Октябрьская, 21",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.000737,
 "lng": 26.408341
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белогорье, ул. Мира, 3 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.621138,
 "lng": 32.58268
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, ул. Патона, 12",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.567361,
 "lng": 34.384832
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Никополь, ул. Богуна, 4",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.292079,
 "lng": 25.935837
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Черновцы, ул. Красноармейская, 55",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.30377,
 "lng": 30.648724
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ильичевск, ул. Александрийская, 6",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.44231,
 "lng": 30.714509
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Малиновского, 51",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.414907,
 "lng": 30.714422
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пр. Маршала Жукова, 5 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.832274,
 "lng": 24.022207
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Львов, ул. Грабовского, 11",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 55.138773,
 "lng": 40.193082
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Белозорье, ул. Ленина, 2 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.485208,
 "lng": 30.746832
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пл. Таможенная, 1/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.450369,
 "lng": 35.059133
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Днепропетровск, пр. Гагарина, 8 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.089913,
 "lng": 36.144259
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Дергачи, ул. Железнодорожная, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.648092,
 "lng": 30.974492
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Мироновка, ул. Элеваторная, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.397466,
 "lng": 30.723186
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, ул. Академика Королева, 72",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.921314,
 "lng": 34.912713
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Магдалиновка, ул. Советская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.79735,
 "lng": 36.718936
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Малиновка, ул. Соича, 5",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.299146,
 "lng": 30.65543
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Ильичевск, ул. Ленина, 33",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.142749,
 "lng": 30.373115
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Шабо, ул. Дзержинского, 10",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.444669,
 "lng": 30.678908
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Центральный Аэропорт",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.349187,
 "lng": 31.122525
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тараща, ул. Шевченко, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.898327,
 "lng": 28.584371
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Бердичев, ул. Шевченка, 23",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.465169,
 "lng": 35.040029
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, ул. Челюскина, 12",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.456874,
 "lng": 35.059461
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Днепропетровск, пр. Карла Маркса, 27 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.440674,
 "lng": 22.717492
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Мукачево, ул. Пушкина, 12/35",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.817555,
 "lng": 35.023375
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Запорожье, ул. Новостроек, 7",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.518659,
 "lng": 30.241656
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Ирпень, ул. Шевченко, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.73949,
 "lng": 37.581027
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Краматорск, пр. Мира, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.839683,
 "lng": 24.029717
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, ул. Леони, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.60811,
 "lng": 22.306568
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ужгород, ул. Гагарина, 42/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.892704,
 "lng": 24.754932
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ивано-Франковск, ул. Юности, 23 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.131932,
 "lng": 30.633259
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Обухов, ул. Каштановая, 25",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.756663,
 "lng": 33.4843
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Ромны, ул. Тельмана, 24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.509856,
 "lng": 37.681148
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Константиновка, бул. Космонавтов, 1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.667738,
 "lng": 27.619198
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чижовка, ул. Чижовская, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.428912,
 "lng": 23.747295
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Меденичи, ул. Дрогобычская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.262541,
 "lng": 24.535396
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Павлов, ул. Юности, 39",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.86322,
 "lng": 30.809368
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Кагарлык, ул. Фрунзе, 99",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.441473,
 "lng": 30.677729
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, Аэропорт",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.427929,
 "lng": 26.981363
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Хмельницкий, ул. Соборная, 16",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.389046,
 "lng": 30.679817
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Мизикевича, ул. Ульяновская, 15/2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.481713,
 "lng": 30.745054
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Польский спуск, 13",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.486024,
 "lng": 30.741419
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пер. Чайковского, 10",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.233794,
 "lng": 28.411295
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Винница, Хмельницкое шоссе, 95",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.468669,
 "lng": 30.71268
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Одесса, ул. Картамищевская, 9 В",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.832645,
 "lng": 23.999098
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Львов, ул. Пастернака, 5",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.811576,
 "lng": 35.007312
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Долинское, ул. Мира, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.762616,
 "lng": 25.367111
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Луцк, пр. Соборности, 11",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.411165,
 "lng": 30.726117
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Люстдорфская дорога, 140/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.443039,
 "lng": 30.743649
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, Фонтанская дорога, 17/19",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.132005,
 "lng": 33.440764
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кременчуг, пр. 50-летия Октября, 78 Б",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.89183,
 "lng": 36.447698
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Коммунист, Учебный городок ХНАУ, 11",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.437599,
 "lng": 30.723927
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Малиновского, 1/1",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.957253,
 "lng": 36.316016
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Маршала Жукова, 2/146",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.011843,
 "lng": 28.500786
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Гуты, ул. Ленина, 29",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.528232,
 "lng": 35.867001
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Павлоград, ул. Горького, 166",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.027227,
 "lng": 36.22582
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Харьков, вул. Отакара Яроша, 24 Б",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.616148,
 "lng": 22.269665
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Ужгород, Словянская набережная, 31",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.672603,
 "lng": 32.643911
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Херсон, ул. Залаэгерсег, 18",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.62734,
 "lng": 22.521758
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Анталовци, ул. Мира, 17 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.467226,
 "lng": 30.717578
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Прохоровская, 47",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.997569,
 "lng": 36.233504
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Харьков, ул. Сумская, 26",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.769929,
 "lng": 30.215441
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Умань, ул. Октябрьской революции, 11 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.440325,
 "lng": 30.710324
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Академика Филатова, 70/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.576359,
 "lng": 30.807101
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Сахарова, 34",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.471527,
 "lng": 30.704751
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Средняя, 83 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.605815,
 "lng": 34.513873
 },
 "accuracy" : 50,
 "name": "Банкомат Украинский капитал",
 "phone_number": "+38 044 205-32-90",
 "address": "Полтава, ул. Пищевиков, 27",
 "types": ["atm"],
 "website": "http://www.ukrcapital.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.511083,
 "lng": 30.7909
 },
 "accuracy" : 50,
 "name": "Банкомат Украинский капитал",
 "phone_number": "+38 044 205-32-90",
 "address": "Бровары, Промузел",
 "types": ["atm"],
 "website": "http://www.ukrcapital.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.510634,
 "lng": 31.328673
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Чернигов, ул. Рокосовского, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.485208,
 "lng": 30.746832
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, пл. Таможенная, 1/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.550746,
 "lng": 25.587313
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Тернополь, ул. Руская, 11",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.515991,
 "lng": 32.196422
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Кировоград, пр. Промышленный, 14",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.515991,
 "lng": 32.196422
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Кировоград, пр. Промышленный, 14",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.848508,
 "lng": 35.126443
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Запорожье, ул. 40-летия Советской Украины, 66/5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.349187,
 "lng": 31.122525
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тараща, ул. Шевченка, 66",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.851778,
 "lng": 24.051743
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Львов, ул. Старознесенская, 24/46",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.972481,
 "lng": 36.240566
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, ул. Георгиевская, 1",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.472968,
 "lng": 36.248524
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Пологи, ул. Ломоносова, 36",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.401154,
 "lng": 33.222843
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Глобино, ул. Карла Маркса, 200 Г",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.978627,
 "lng": 31.979468
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Николаев, ул. Никольская, 24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.47772,
 "lng": 36.258462
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Пологи, ул. Киреева, 9",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.882209,
 "lng": 33.384275
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Орджоникидзе, 9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.460876,
 "lng": 35.050641
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Днепропетровск, бул. Катеринославский, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 45.619172,
 "lng": 38.913734
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Первомайское, ул. Заводская, 2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.899603,
 "lng": 36.195432
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, вул. Энгельса, 21",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.480068,
 "lng": 30.737657
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Жуковского, 30",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.406878,
 "lng": 30.720921
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Академика Королева, 24",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.435352,
 "lng": 30.729792
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Краснова, 6/1",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.289303,
 "lng": 25.934079
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Черновцы, ул. Головна, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 51.489879,
 "lng": 31.302084
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Чернигов, пр. Мира, 17",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.0083,
 "lng": 36.239303
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Харьков, ул. Каразина, 2",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.459963,
 "lng": 30.711186
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Одесса, ул. Михайловская, 44",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.908233,
 "lng": 33.344704
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, пр. Карла Маркса, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.233675,
 "lng": 28.439888
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Винница, Хмельницкое шоссе, 25",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.037656,
 "lng": 24.356538
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Калуш, ул. Богдана Хмельницкого, 30",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.093746,
 "lng": 37.558763
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Мариуполь, пр. Миру, 14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.678023,
 "lng": 30.991155
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Мироновка, ул. Фрунзе, 16",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.797228,
 "lng": 35.197505
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Николаевка, ул. Коцюбы, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.472968,
 "lng": 36.248524
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Пологи, ул. Ломоносова, 36",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 46.484025,
 "lng": 30.733163
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Одесса, ул. Преображенская, 34",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.755875,
 "lng": 27.218799
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Староконстантинов, ул. Острожского, 2",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.09349,
 "lng": 33.437232
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Знамянка, ул. Матросова, 28 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.049703,
 "lng": 36.294599
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Жуковского, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.225818,
 "lng": 28.448287
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Винница, ул. Пирогова, 49",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.170237,
 "lng": 30.719736
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Плюты, ул. Малышка, 27",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.965066,
 "lng": 33.436857
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, пр. 200-летия Кривого Рога, 7 В",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 47.900418,
 "lng": 33.3983
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Кривой Рог, ул. Косиора, 33 В",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.984398,
 "lng": 36.26944
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, ул. Фесенковская, 16",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.016045,
 "lng": 36.357881
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Харьков, пр. Тракторостроителей, 142",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.875268,
 "lng": 23.880764
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Подрясное, ул. Европейская, 1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.64166,
 "lng": 30.417854
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Старые Петровцы, ул. Полевая, 17",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 48.471973,
 "lng": 29.233594
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Тростянец, ул. Набережная, 28 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 49.626073,
 "lng": 29.056794
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Немиринцы, ул. Центральная, 41",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.623121,
 "lng": 26.249798
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Ровно, ул. Симона Петлюры, 22",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.463084,
 "lng": 30.458901
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Дегтяревская, 38/42",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.404095,
 "lng": 30.523594
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, пр. Науки, 8",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.396359,
 "lng": 30.629176
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Михаила Гришко, 4",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.469206,
 "lng": 30.457584
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Семьи Хохловых, 15",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.46379,
 "lng": 30.458943
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Дегтяревская, 38",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44029,
 "lng": 30.483249
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Лукашевича, 15 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.460386,
 "lng": 30.348188
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Ирпенская, 76",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.502595,
 "lng": 30.591724
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, пр. Маяковского, 17",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.396015,
 "lng": 30.63107
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Михаила Гришко, 5",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.395903,
 "lng": 30.63243
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Михаила Гришко, 3 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44001,
 "lng": 30.501663
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Саксаганского, 74",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.512872,
 "lng": 30.504806
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Тимошенко, 29",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.43563,
 "lng": 30.607129
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Серафимовича, 16",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.469317,
 "lng": 30.508561
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Константиновская, 34 Б",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.431211,
 "lng": 30.516039
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Большая Васильковская, 54",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.500835,
 "lng": 30.496776
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Малиновского, 12",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.428467,
 "lng": 30.538475
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, бул. Леси Украинки, 19/16 A",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.413177,
 "lng": 30.526274
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Большая Васильковская, 143/2",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.457979,
 "lng": 30.405865
 },
 "accuracy" : 50,
 "name": "Банкомат Украинский капитал",
 "phone_number": "+38 044 205-32-90",
 "address": "Киев, пр. Победы, 67",
 "types": ["atm"],
 "website": "http://www.ukrcapital.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.432237,
 "lng": 30.515112
 },
 "accuracy" : 50,
 "name": "Банкомат Украинский капитал",
 "phone_number": "+38 044 205-32-90",
 "address": "Киев, ул. Большая Васильковская, 72",
 "types": ["atm"],
 "website": "http://www.ukrcapital.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.444724,
 "lng": 30.410815
 },
 "accuracy" : 50,
 "name": "Банкомат Украинский капитал",
 "phone_number": "+38 044 205-32-90",
 "address": "Киев, бул. Ивана Лепсе, 8",
 "types": ["atm"],
 "website": "http://www.ukrcapital.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.461938,
 "lng": 30.479295
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Киев, ул. Дегтяревская, 4 А",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.513209,
 "lng": 30.51054
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, пр. Героев Сталинграда, 26 A",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.419758,
 "lng": 30.554359
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, пер. Мичурина 3/2 А",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.451654,
 "lng": 30.412798
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Радищева, 3",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.466981,
 "lng": 30.405296
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Щербакова, 35",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.434617,
 "lng": 30.506889
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Жилянская, 48",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.406164,
 "lng": 30.614323
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, Днепровская набережная, 25",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.485984,
 "lng": 30.467814
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Петропавловская, 6",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.439045,
 "lng": 30.498883
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Жилянская, 75 (Л)",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445982,
 "lng": 30.512824
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Богдана Хмельницкого, 19/21",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.439045,
 "lng": 30.498883
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Жилянская, 75 (П)",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.39131,
 "lng": 30.503188
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Маршала Конева, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.51739,
 "lng": 30.616699
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Маяковского, 75/2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4501,
 "lng": 30.5234
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Стретенская, 7/9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.452707,
 "lng": 30.456431
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 37, кор.7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.440086,
 "lng": 30.517354
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Большая Васильковская, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.430407,
 "lng": 30.383454
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Леся Курбаса, 6 Г",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.523599,
 "lng": 30.478506
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Лебединская, 4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.380942,
 "lng": 30.476499
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Академика Глушкова, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.41651,
 "lng": 30.519012
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Казимира Малевича, 107",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449064,
 "lng": 30.465277
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Политехническая, 6",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.505936,
 "lng": 30.469629
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Луговая, 13",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.451396,
 "lng": 30.482976
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Черновола, 28/1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.435901,
 "lng": 30.631164
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Харьковское шоссе",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.380942,
 "lng": 30.476499
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Академика Глушкова, 2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445163,
 "lng": 30.535373
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Институтская, 22/7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.466954,
 "lng": 30.514242
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Верхний Вал, 32",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.446872,
 "lng": 30.489858
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 28/1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.470648,
 "lng": 30.467699
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Мельникова, 36/1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.414198,
 "lng": 30.661778
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Харьковское шоссе, 168",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.441439,
 "lng": 30.48029
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Воздухофлотский, 7",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445604,
 "lng": 30.497638
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, бул. Тараса Шевченко, 27",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.405256,
 "lng": 30.631426
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Григоренка, 23",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.466543,
 "lng": 30.470076
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Якира, 12/42",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449306,
 "lng": 30.460681
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 37, кор.1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.45068,
 "lng": 30.455048
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 37, кор.4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.454583,
 "lng": 30.614085
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Попудренко, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.385698,
 "lng": 30.480591
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Васильковская, 49",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.521976,
 "lng": 30.500806
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Героев Днепра, 30",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.402436,
 "lng": 30.514841
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Голосеевский, 48",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.444339,
 "lng": 30.415215
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Героев Севастополя, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.501154,
 "lng": 30.454066
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Попова, 2 В",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.426579,
 "lng": 30.367309
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Зодчих, 46",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.501796,
 "lng": 30.594168
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Маяковского, 8",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.411185,
 "lng": 30.549731
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Киквидзе, 23",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.437828,
 "lng": 30.538203
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Кловский спуск, 9/2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.475308,
 "lng": 30.510471
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Набережно-Луговая",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.399474,
 "lng": 30.649999
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Бажана, 36",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.427938,
 "lng": 30.457248
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, бул. Чоколовский, 9/13",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.448867,
 "lng": 30.521582
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Крещатик, 26",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.448867,
 "lng": 30.521582
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Крещатик, 26",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.456112,
 "lng": 30.382877
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 93",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.412685,
 "lng": 30.39689
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Симиренко, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.459384,
 "lng": 30.63314
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Попудренко, 50",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44307,
 "lng": 30.622628
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Мира, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.416897,
 "lng": 30.65052
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Тростянецкая, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.461792,
 "lng": 30.346563
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Чернобыльская, 18",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.479759,
 "lng": 30.406232
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Щербакова, 72",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.490258,
 "lng": 30.601077
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Курнатовского, 19",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.437244,
 "lng": 30.631898
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Харьковское шоссе, 11 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.423158,
 "lng": 30.482765
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Соломенская, 19",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.502553,
 "lng": 30.605234
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Драйзера, 8",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.477711,
 "lng": 30.626401
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Милютенко, 23",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.457489,
 "lng": 30.395292
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 79",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.504683,
 "lng": 30.428555
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Правды, 66",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.509806,
 "lng": 30.595665
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Драйзера, 21",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.443165,
 "lng": 30.523259
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Круглоуниверситетская, 3-5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.437272,
 "lng": 30.547023
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Суворова, 9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.486463,
 "lng": 30.519392
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Московский , 34 В",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445151,
 "lng": 30.444187
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Борщаговская, 154",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.383636,
 "lng": 30.488042
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Героев Обороны, 5",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.487572,
 "lng": 30.515753
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Московский, 28",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.437828,
 "lng": 30.538203
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Кловский спуск, 9/2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.435502,
 "lng": 30.598176
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, бул. Давыдова, 3",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.441855,
 "lng": 30.43486
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Борщаговская, 189",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.461462,
 "lng": 30.479194
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Дегтяревская, 9",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.453168,
 "lng": 30.447251
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Победы, 47",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.447688,
 "lng": 30.457358
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Политехническая, 14",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.520015,
 "lng": 30.452712
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Автозаводская, 99/4 А",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.400799,
 "lng": 30.61398
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, Днепровская набережная, 16",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445731,
 "lng": 30.513276
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Владимирская, 60",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.512454,
 "lng": 30.422221
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Свободы, 15/1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.447549,
 "lng": 30.518813
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Пушкинская, 24",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4501,
 "lng": 30.5234
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Порика",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.396961,
 "lng": 30.492132
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Казачья, 120/4 E",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.396378,
 "lng": 30.614903
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Бажана, 1 Е",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.48995,
 "lng": 30.495512
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Московский, 23",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.403023,
 "lng": 30.62282
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Урловская, 1/8",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.495283,
 "lng": 30.512315
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Мате Залки, 6",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.441806,
 "lng": 30.520134
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Большая Васильковская, 1-3/2",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.503353,
 "lng": 30.507193
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Малиновского, 34",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.458022,
 "lng": 30.379381
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, бул. Вернадского, 4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.468538,
 "lng": 30.522004
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Спасская, 30 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.439045,
 "lng": 30.498883
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Жилянская, 75",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.454277,
 "lng": 30.597535
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Луначарского, 10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.447588,
 "lng": 30.422271
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, бул. Ивана Лепсе, 6/З",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.440019,
 "lng": 30.515826
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Пушкинская, 42/4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.461467,
 "lng": 30.357539
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Академика Палладина, 22",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.447265,
 "lng": 30.459259
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Политехническая, 39",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.513126,
 "lng": 30.494155
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Тимошенко, 21",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.447293,
 "lng": 30.458542
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Политехническая, 16",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.486535,
 "lng": 30.471247
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Фрунзе, 109 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.452568,
 "lng": 30.516016
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Владимирская, 23 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.485415,
 "lng": 30.515751
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Московский, 28 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.489754,
 "lng": 30.489512
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Московский, 13 В",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4063,
 "lng": 30.535404
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, Железнодорожное шоссе, 6",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.506419,
 "lng": 30.510235
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Героев Сталинграда, 16 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.475425,
 "lng": 30.49018
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Фрунзе, 74",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.453329,
 "lng": 30.424879
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пер. Чугуевский, 21",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.442423,
 "lng": 30.624097
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Воссоединения, 2/1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.461623,
 "lng": 30.354708
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Академика Палладина, 7 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.517068,
 "lng": 30.450134
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Вышгородская, 50",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.507845,
 "lng": 30.609192
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Маяковского, 26",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.466962,
 "lng": 30.471408
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Мельникова, 75",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.350966,
 "lng": 30.540576
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Краснознаменная, 137",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.427928,
 "lng": 30.531794
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Коновальца, 32 Б",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.500835,
 "lng": 30.496776
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Малиновского, 12",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.426754,
 "lng": 30.601334
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Тычины, 16/2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4513,
 "lng": 30.506528
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Олеся Гончара, 41",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.440019,
 "lng": 30.515826
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Пушкинская, 42/4",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.450309,
 "lng": 30.468858
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Победы, 29",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.439344,
 "lng": 30.52549
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Бассейная, 23",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.4201,
 "lng": 30.453876
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Воздухофлотский, 50/2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.40181,
 "lng": 30.63668
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Драгоманова, 29",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.457639,
 "lng": 30.398405
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Победы, 75/2",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44929,
 "lng": 30.463536
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, пр. Победы, 37",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.451772,
 "lng": 30.488933
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Дмитриевская, 37 А",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.434133,
 "lng": 30.506748
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Жилянская, 43",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.451109,
 "lng": 30.521492
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Софиевская, 12",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.471012,
 "lng": 30.516202
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Ярославская, 47/29",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.434133,
 "lng": 30.506748
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Жилянская, 43",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.420603,
 "lng": 30.52041
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Большая Васильковская, 116",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.457084,
 "lng": 30.372522
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, пр. Победы, 128/2",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.485341,
 "lng": 30.483106
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Константиновская, 15",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.424357,
 "lng": 30.541938
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Щорса, 44",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.450061,
 "lng": 30.595562
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Раисы Окипной, 4",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.423409,
 "lng": 30.507927
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Николая Гринченка, 4 В",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.510953,
 "lng": 30.505275
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Тимошенко, 18",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.438959,
 "lng": 30.519448
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Шота Руставели, 16",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.451616,
 "lng": 30.522662
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Михайловская, 2",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.422364,
 "lng": 30.505954
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Амосова, 12",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.434133,
 "lng": 30.506748
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Жилянская, 43",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.431833,
 "lng": 30.50761
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Физкультуры, 28",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449731,
 "lng": 30.500563
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Олеся Гончара, 62",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445907,
 "lng": 30.501593
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, бул. Тараса Шевченко, 38/40",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.456265,
 "lng": 30.492099
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Артема, 52",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.399034,
 "lng": 30.510676
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, пр. Голосеевский, 68",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.444891,
 "lng": 30.415471
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, бул. Ивана Лепсе, 29",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.469352,
 "lng": 30.446238
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Е. Телиги, 11",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.422364,
 "lng": 30.505954
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Амосова, 12",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.441617,
 "lng": 30.621647
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Воссоединения, 8/2",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.394832,
 "lng": 30.620157
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Бажана, 10",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.450287,
 "lng": 30.521698
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Бориса Гринченко, 1",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.423446,
 "lng": 30.518642
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Большая Васильковская, 114",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.467391,
 "lng": 30.510643
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Ярославская, 15/23",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.444196,
 "lng": 30.362225
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Победы, 7",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449819,
 "lng": 30.593255
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Раисы Окипной, 4 А",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.513126,
 "lng": 30.494155
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Тимошенко, 21",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.47098,
 "lng": 30.664948
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Броварской, 17",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.445151,
 "lng": 30.444187
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Борщаговская, 154 А",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.469794,
 "lng": 30.466263
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Киев, ул. Мельникова, 83 Д",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.430144,
 "lng": 30.516444
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Киев, ул. Большая Васильковская, 65",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.513126,
 "lng": 30.494155
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Киев, ул. Маршала Тимошенко, 21",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.421299,
 "lng": 30.59378
 },
 "accuracy" : 50,
 "name": "Банкомат Банк инвестиций и сбережений",
 "phone_number": "+38(044)207-70-20",
 "address": "Киев, ул. Березняковская, 31",
 "types": ["atm"],
 "website": "http://www.bisbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.463452,
 "lng": 30.452857
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Дегтяревская, 48",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.417174,
 "lng": 30.406943
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Якутская, 8",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.436394,
 "lng": 30.518006
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Шота Руставели, 40/10",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.428033,
 "lng": 30.508035
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Федорова, 32 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.468538,
 "lng": 30.522004
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Спасская, 30 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.446142,
 "lng": 30.514296
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Богдана Хмельницкого, 26",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.444608,
 "lng": 30.492778
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Киев, ул. Жилянская, 107",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.404067,
 "lng": 30.404748
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, Кольцевая дорога, 20/1 А",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.458604,
 "lng": 30.396464
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, пр. Победы, 98/2",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.394467,
 "lng": 30.493638
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Васильковская, 24",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.469777,
 "lng": 30.512536
 },
 "accuracy" : 50,
 "name": "Банкомат ВиЭс Банк",
 "phone_number": "0 800 500 260",
 "address": "Киев, ул. Щекавицкая, 30/39",
 "types": ["atm"],
 "website": "http://www.vsbank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.475416,
 "lng": 30.489602
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Фрунзе, 63",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.475425,
 "lng": 30.49018
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Фрунзе, 74",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.433801,
 "lng": 30.509593
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Жилянская, 31",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.343115,
 "lng": 30.544959
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, ул. Академика Заболотного, 37",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.439335,
 "lng": 30.496029
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Льва Толстого, 57",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.450872,
 "lng": 30.453923
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Академика Янгеля, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.519057,
 "lng": 30.501788
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Оболонский, 36 Б",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.450309,
 "lng": 30.468858
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, пр. Победы, 29",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.458367,
 "lng": 30.614149
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Малышко, 3",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.393338,
 "lng": 30.486396
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Васильковская, 34",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.423409,
 "lng": 30.507927
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Николая Гринченка, 4 В",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.428831,
 "lng": 30.59935
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, пр. Тычины, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.416014,
 "lng": 30.539294
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, бул. Дружбы народов, 17/5",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.424926,
 "lng": 30.506753
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Николая Гринченка, 2/1",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.416482,
 "lng": 30.540182
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, бул. Дружбы народов, 19",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.517582,
 "lng": 30.597897
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Лаврухина, 4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.424013,
 "lng": 30.51645
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Антоновича, 97",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.438959,
 "lng": 30.519448
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, ул. Шота Руставели, 16",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.417271,
 "lng": 30.51675
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Казимира Малевича, 86 Г",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.434567,
 "lng": 30.501386
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Гайдара, 58/10",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.397648,
 "lng": 30.507147
 },
 "accuracy" : 50,
 "name": "Банкомат Платинум",
 "phone_number": " 0800 308 308",
 "address": "Киев, ул. Васильковская, 2",
 "types": ["atm"],
 "website": "http://ua.platinumbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.416564,
 "lng": 30.618956
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Здолбуновская, 4",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.507387,
 "lng": 30.440181
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Западинская, 15",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.488782,
 "lng": 30.496286
 },
 "accuracy" : 50,
 "name": "Банкомат Пивденный",
 "phone_number": "0 800 30 70 30",
 "address": "Киев, пр. Московский, 10",
 "types": ["atm"],
 "website": "http://bank.com.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44959,
 "lng": 30.610407
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Беломорская, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.44959,
 "lng": 30.610407
 },
 "accuracy" : 50,
 "name": "Банкомат Правекс-Банк",
 "phone_number": "0 800 500 450",
 "address": "Киев, ул. Беломорская, 1",
 "types": ["atm"],
 "website": "http://www.pravex.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.403758,
 "lng": 30.629776
 },
 "accuracy" : 50,
 "name": "Банкомат Идея Банк",
 "phone_number": "0 800 50 20 30 ",
 "address": "Киев, ул. Княжий Затон, 2/30",
 "types": ["atm"],
 "website": "http://www.ideabank.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449333,
 "lng": 30.410283
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Радищева, 10/14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.466981,
 "lng": 30.405296
 },
 "accuracy" : 50,
 "name": "Банкомат БТА Банк",
 "phone_number": "0-800-30-45-45 ",
 "address": "Киев, ул. Щербакова, 35",
 "types": ["atm"],
 "website": "btabank.ua",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.449333,
 "lng": 30.410283
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Радищева, 10/14",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.43668,
 "lng": 30.544827
 },
 "accuracy" : 50,
 "name": "Банкомат Креди Агриколь",
 "phone_number": "+380 44 495 22 77",
 "address": "Киев, ул. Московская, 32/34",
 "types": ["atm"],
 "website": "https://credit-agricole.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
r = requests.post(post_url, json={"location": {
 "lat": 50.395123,
 "lng": 30.478717
 },
 "accuracy" : 50,
 "name": "Банкомат ОТП Банк",
 "phone_number": "+38 044 490 05 00",
 "address": "Киев, пер. Ахтирський, 7",
 "types": ["atm"],
 "website": "https://www.otpbank.com.ua/",
 "language": "ru"
 })
print(r.status_code)
print(r.json())
