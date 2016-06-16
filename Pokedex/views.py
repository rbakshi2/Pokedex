from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import requests
import json

BASE_URL = 'http://pokeapi.co'


def query_pokeapi(resource_uri):
    url = '{0}{1}'.format(BASE_URL, resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None


def pokemon(request):

    body = request.GET.get("q")
    body = body.lower()

    pokemon_url = '/api/v1/pokemon/{0}/'.format(body)
    pokemonn = query_pokeapi(pokemon_url)

    if pokemonn:
        sprite_uri = pokemonn['sprites'][0]['resource_uri']
        description_uri = pokemonn['descriptions'][0]['resource_uri']

        sprite = query_pokeapi(sprite_uri)
        description = query_pokeapi(description_uri)

        message = '{0}, {1}'.format(pokemonn['name'], description['description'])
        image = '{0}{1}'.format(BASE_URL, sprite['image'])
        html="<html><body> %s </html>" % message
        return HttpResponse(html)



def home_page(request):
    return render_to_response("index.html")
