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
        effect = abilitiess['effect_entries'][0]['effect']
        name = abilitiess['name']
        html ="<html><body> <br> Name: %s <br> Description: %s <body> </html>" % (name, effect)

        return HttpResponse(html)

def item(request):

    body = request.GET.get("q", "Something went wrong")
    body = body.lower()

    item_url = '/api/v2/item/{0}/'.format(body)
    itemm = query_pokeapi(item_url)

    if itemm:

        name = itemm['name']
        cost = itemm['cost']
        effect = itemm['effect_entries'][0]['effect']
        html ="<html><body> <br> Name: %s <br> Description: %s  <br> Cost: %s<body> </html>" % (name, effect, cost)

        return HttpResponse(html)


def type(request):

    body = request.GET.get("q", "Something went wrong")
    body = body.lower()

    type_url = '/api/v2/type/{0}/'.format(body)
    typee = query_pokeapi(type_url)

    if typee:

        typeee = typee['damage_relations']
        ndt_name = typeee['no_damage_to']
        hdt_name = typeee['half_damage_to']
        ddt_name = typeee['double_damage_to']
        ndf_name = typeee['no_damage_from']
        hdf_name = typeee['half_damage_from']
        ddf_name = typeee['double_damage_from']

        name = typee['name']
        
        html ="<html><body> <br> Name: %s <br>No damage to %s <br>half damage to %s <br>double damage to %s   <br>No damage from %s <br>half damage from %s <br>double damage from %s <body> </html>" % (name, ndt_name, hdt_name, ddt_name, ndf_name, hdf_name, ddf_name)

        return HttpResponse(html)


def home_page(request):
    return render_to_response("index.html")
