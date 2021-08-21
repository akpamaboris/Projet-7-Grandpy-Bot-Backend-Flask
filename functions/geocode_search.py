import googlemaps


def geocodesearch(search):


    # Je commence à m'occuper des cartes
    API_KEY = 'AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU'
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode(search)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    destination = gmaps.places(query=search)
    destination_finale = destination['results'][0]["formatted_address"]
    result_google = {"lat": lat, "lng": lng, "destination": destination_finale}
    return result_google
