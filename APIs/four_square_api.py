import pprint
import requests
import pandas as pd
from APIs.geocoder_api import findCoordinates

def search_api(zip, query):
    lat_lng_tuple = findCoordinates(zip)
    latlng = str(lat_lng_tuple[0]) + ',' + str(lat_lng_tuple[1])
    api_key =  ""
    search_query = query
    radius = 32186 #this is 20 miles
    limit = 15
    url = 'https://api.foursquare.com/v3/places/nearby?ll={}&query={}&radius={}&limit={}'.format(latlng, search_query, radius, limit)
    headers = {
        "Accept": "application/json",
        "Authorization": api_key
    }
    results = requests.get(url,headers=headers).json()
    #pprint.pprint(results)
    item_length = len(results['results'])
    #print(item_length)
    if not results['results']: #If there is no information
        empty = pd.DataFrame()
        return empty
    else: #If query is one of the given options
        data_list = [] #list of dictionaries
        for i in range(item_length):
            data_dict = {}
            try:
                id = results['results'][i]['categories'][0]['id']
            except:
                id = "0000"
            name = results['results'][i]['name']
            try:
                address_list = results['results'][i]['location']['address'] + " " + \
                               results['results'][i]['location']['locality'] + " " + \
                               results['results'][i]['location']['region'] + " " + \
                               results['results'][i]['location']['postcode']
            except:
                address_list = name

            lat_lng = str(results['results'][i]['geocodes']['main']['latitude']) + ',' + str(results['results'][i]['geocodes']['main']['longitude'])

            fsq_id = results['results'][i]['fsq_id']
            picture_results = requests.get(url = "https://api.foursquare.com/v3/places/{}/photos?limit=1&classifications=food%2Cindoor%2Cmenu%2Coutdoor".format(fsq_id), headers=headers).json()
            #pprint.pprint(picture_results)
            if len(picture_results)  == 0:
                pic = "/static/img/foodimage.jpg"
            else:
                pic = picture_results[0]['prefix'] +"300x300" + picture_results[0]['suffix']
            NAME = "Name"
            ADDRESS = "Address"
            ID = "Id"
            PICTURE = "Picture"
            LATLNG = "Latitude_Longitude"
            data_dict[NAME] = name
            data_dict[ADDRESS] = address_list
            data_dict[ID] = id
            data_dict[PICTURE] = pic
            data_dict[LATLNG] = lat_lng
            data_list.append(data_dict) #
        df = pd.DataFrame.from_records(data_list, index=None)
        return df
#search_api(19047,"bestBuy")
