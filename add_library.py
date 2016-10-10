from googleplaces import GooglePlaces, types, lang
import googlemaps

YOUR_API_KEY = 'AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag'
gmaps = googlemaps.Client(key='AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag')

google_places = GooglePlaces(YOUR_API_KEY)

print(google_places.get_place(place_id='qgYvCi0wMDAwMDBjNmVlMjk0ZDM0OjQwYzdlZGFiNjQzOmZlZmZhOWMyNzMzZDUwMzI'))

#google_places.delete_place(place_id='qgYvCi0wMDAwMDBjNmVlMjk0ZDM0OjQwZDRjZTgyYWFmOjRmZDhlMDg4YTc5NTE1MGM')

