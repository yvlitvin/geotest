from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyC9a-jaBIbXokxx9dIz7aTP9jbOjLCC9ag'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location='Николаев, пр. Центральный, 27 Б',
        radius=20, types=[types.TYPE_ATM])
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogsp
# ot.com.au/2016/02/changes-and-quality-improvements-in_16.html

if query_result.has_attributions:
    print (query_result.html_attributions)



for place in query_result.places:
    # Returned places from a query are place summaries.
    print (place.name)
    print (place.geo_location)
    print (place.place_id)

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print (place.details) # A dict matching the JSON response from Google.
    print (place.local_phone_number)
    print (place.international_phone_number)
    print (place.website)
    print (place.url)



