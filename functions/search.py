import wikipedia
import json

# i import the functions needed for this project

from functions import parser
from functions import geocode_search

def searchword(str) :




    # i use my parser function

    finalresearch = parser.parser(str)

    list_words_random_answer = ['bonjour', 'ça va', 'hey', 'salut', 'grandpy']

    response ={'result':'grandpy Bot te salue'}
    json_data_salutation = json.dumps(response, ensure_ascii=False)
    for i in list_words_random_answer:
        if i.__contains__(finalresearch):
            return json_data_salutation



    # placeid_response = response['candidates'][0]['place_id']
    # Geocoding an address





    # I set the search language in french
    wikipedia.set_lang("fr")
    print("final search is ")
    print(finalresearch)

    # display the result of the original search
    result = wikipedia.summary(finalresearch, sentences=3)
    test = wikipedia.search(finalresearch)
    page = wikipedia.page(finalresearch)
    result_google = geocode_search.geocodesearch(finalresearch)
    print('result_google',result_google)
    print('result_google lat',result_google['lat'])
    url_search = page.url
    print('page', page.url)
    print("test for search", test)
    print("result is", result)
    data = {"result": result, "lat": result_google['lat'], "lng": result_google['lng'], "url": url_search,
            "destination": result_google['destination']}
    json_data = json.dumps(data, ensure_ascii=False)



    #display some suggestion
    #searchResult = wikipedia.search(str(searchRequest), results=10, suggestion=True)
    #print(searchResult)
    return json_data
    #return result

