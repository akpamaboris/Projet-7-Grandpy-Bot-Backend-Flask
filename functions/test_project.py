
from functions import parser
from functions import geocode_search
import wikipedia



import urllib.request

from io import BytesIO
import json


def test_http_return(monkeypatch):
    results = {'lat': 38.8899389, 'lng': -77.0090505, 'destination': '55 Rue du Faubourg Saint-Honoré, 75008 Paris, France'}
    def mockreturn(requests):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert geocode_search.geocodesearch('emmanuel macron quelle adresse') == results

def test_wiki(monkeypatch):
    results = ['Emmanuel Macron', 'Brigitte Macron', 'Opinion polling on the Emmanuel Macron presidency', 'La République En Marche!', '2017 French presidential election', 'Macron', 'Protests against Emmanuel Macron', 'Jean-Michel Macron', 'Murder of Samuel Paty', 'Laurence Auzière-Jourdan']
    def mockreturn(requests):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert len(wikipedia.search('emmanuel macron')) == len(results)


def test_parser():
    assert parser.parser("qui est emmanuel macron ?") == "emmanuel macron"

def test_parser2():
    assert parser.parser("qui est vladimir poutine?") == "vladimir poutine"

def test_geocode():
    assert geocode_search.geocodesearch('emmanuel macron quelle adresse') == \
           {'lat': 38.8899389, 'lng': -77.0090505, 'destination': '55 Rue du Faubourg Saint-Honoré, 75008 Paris, France'}


