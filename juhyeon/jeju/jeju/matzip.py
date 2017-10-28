#--*- coding: utf-8 -*-
from urllib import parse
from geolocation.main import GoogleMaps
from googleplaces import GooglePlaces, types, lang
from math import radians, cos, sin, asin, sqrt
from urllib.request import urlopen
import json
import random
import sys
rankeys=["AIzaSyA7FyX4lDBiYsCG_KeOm5g-NmXqOmwWoeQ","AIzaSyCIJgbczxaPNjRWMvIXlQhNjUWAT7TtquQ","AIzaSyCHFFfOhqJdNfvclloArU1lhieenbuDyTk","AIzaSyAf3lfCaL7fROslPiLQIvMX8lbX9IVZ9m0"]
def nonchcker(obj):
    if obj is None:
        return "There ain't sucha place"
    else:
        return str(obj)

def distancer(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

def search(param):
    YOUR_API_KEY = random.choice(rankeys)
    google_maps = GoogleMaps(YOUR_API_KEY)
    google_places = GooglePlaces(YOUR_API_KEY)
    ans=param+" restaurants."
    origins = param
    #origins = origins.decode('utf-8')
    prefix = "http://maps.googleapis.com/maps/api/geocode/json?address="
    location = param
    postfix = "&sensor=false"
    urlData = prefix + parse.quote(location.encode('UTF-8')) + postfix
    webUrl = urlopen(urlData)
    if (webUrl.getcode() == 200):
        data = webUrl.read().decode('utf-8')
        j = json.loads(data)
        try:
            lat1=(j["results"][0]["geometry"]["location"]["lat"])
            lon1=(j["results"][0]["geometry"]["location"]["lng"])
        except:
            lat1=33.5003192
            lon1=126.5278462
    try:
        query_result = google_places.radar_search(
                location=origins,
                radius = 300,
                language ='ko',
            keyword = 'restaurant',
                types=[types.TYPE_FOOD,types.TYPE_RESTAURANT]
                )
    except:
        query_result = google_places.radar_search(
            location="제주창조경제혁신센터",
            radius=300,
            language='ko',
            keyword='restaurant',
            types=[types.TYPE_FOOD, types.TYPE_RESTAURANT]
        )
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:
    # http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

    #if query_result.has_attributions:
    #    print(query_result.html_attributions)
    rst=""
    result={}
    data=[]
    ans=query_result.places
    for ind,place in enumerate(ans):
            place.get_details()
            destination = place.geo_location
            if ind>9:
                break
            content={}
            # rst+=("####["+str(ind+1)+": "+place.name+"]##")
            content['name']=(str(ind + 1) + ": " + place.name)
            distance =distancer(lon1,lat1,float(destination['lng']),float(destination['lat']))*1000
            # rst += "##dstance: " +str(round(distance,2))+"m"
            content['distance']=str(round(distance,2))+"m"
            # rst +="##phone: "+str(place.local_phone_number)
            content['phone']=str(place.local_phone_number)
            # rst +="##route: maps.google.com/?daddr="+str(destination['lat'])+","+str(destination['lng'])
            # content['find']="http://maps.google.com/?daddr="+str(destination['lat'])+","+str(destination['lng'])
            # rst += "##address: " + str(place.formatted_address)
            content['addr']=str(place.formatted_address)
            content['lat']=str(destination['lat'])
            content['lng'] = str(destination['lng'])
            data.append(content)
    result['data']=data
    result['status']=len(ans)
    return result
