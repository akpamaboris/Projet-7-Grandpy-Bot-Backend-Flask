import googlemaps
# importing required modules
import requests, json
def geocodesearch(search):
    
    try:


        # Je commence à m'occuper des cartes
        API_KEY = 'AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU'
        
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        #gmaps = googlemaps.Client(key=API_KEY)
        # geocode_result = gmaps.geocode(search)
        #print('geocode_result',geocode_result)
        r = requests.get(url + 'query=' + search +
                        '&key=' + API_KEY)
  
        # json method of response object convert
        #  json format data into python format data
        x = r.json()
        print('I PRINT xxxxxxxxxxxx', x)
        print('I PRINT adrrrrrrrrrrressssssssss',x['results'][0]["formatted_address"])
        print('I PRINT laaaaaaaaaaat',x['results'][0]['geometry']['location']['lat'])
        x_lat = x['results'][0]['geometry']['location']['lat']
        x_lng= x['results'][0]['geometry']['location']['lng']
        x_address = x['results'][0]["formatted_address"]
  
        #lat = geocode_result[0]['geometry']['location']['lat']
        #lng = geocode_result[0]['geometry']['location']['lng']
        #destination = gmaps.places(query=search)
        #destination_finale = destination['results'][0]["formatted_address"]
        result_google = {"lat": x_lat, "lng": x_lng, "destination": x_address}
        return result_google

    except:
        return {"lat": 0, "lng": 0, "destination": '0 rue du 0'}