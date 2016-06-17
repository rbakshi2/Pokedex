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

    body = request.GET.get("q", "Something went wrong")
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
        html ="<html><body> <img src=\"%s\"> <br> %s <body> </html>" % (image, message)

        return HttpResponse(html)


def abilities(request):

    body = request.GET.get("q", "Something went wrong")
    body = body.lower()

    abilities_url = '/api/v2/ability/{0}/'.format(body)
    abilitiess = query_pokeapi(abilities_url)

    if abilitiess:
        # #sprite_uri = pokemonn['sprites'][0]['resource_uri']
        # description_uri = abilitiess['description'][0]['resource_uri']
        #
        # #sprite = query_pokeapi(sprite_uri)
        # description = query_pokeapi(description_uri)
        #s
        # message = '{0}, {1}'.format(abilitiess['name'], description['description'])
        # #image = '{0}{1}'.format(BASE_URL, sprite['image'])
        effect_entries = abilitiess['effect_entries']
        pokemonnn = abilitiess['pokemon']
        html ="<html><body>  <br> %s<br> %s <body> </html>" % (effect_entries, pokemonnn)

        return HttpResponse(html)


def type(request):

    body = request.GET.get("q", "Something went wrong")
    body = body.lower()

    type_url = '/api/v1/type/{0}/'.format(body)
    typee = query_pokeapi(type_url)

    if typee:
        # sprite_uri = typee['sprites'][0]['resource_uri']
        # description_uri = typee['descriptions'][0]['resource_uri']
        #
        # sprite = query_pokeapi(sprite_uri)
        # description = query_pokeapi(description_uri)

        super_effective_uri = typee['super_effective'][0]['resource_url']
        super_effective = query_pokeapi(super_effective_uri)

        # message = '{0}, {1}'.format(pokemonn['name'], description['description'])
        # image = '{0}{1}'.format(BASE_URL, sprite['image'])
        html ="<html><body> <img src=\"%s\"> <br> %s <body> </html>" % super_effective

        return HttpResponse(html)


def home_page(request):
    return render_to_response("index.html")
