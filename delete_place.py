
import requests

post_url = "https://maps.googleapis.com/maps/api/place/delete/json?key=AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag"

r = requests.post(post_url, json={
"place_id": 'qgYvCi0wMDAwMDBjNmVlMjk0ZDM0OjQwZDRjZTgyYWFmOjRmZDhlMDg4YTc5NTE1MGM'

 })


print(r.status_code)
print(r.json())

#google_places.delete_place(place_id='qgYvCi0wMDAwMDBjNmVlMjk0ZDM0OjQwZDRjZTgyYWFmOjRmZDhlMDg4YTc5NTE1MGM')