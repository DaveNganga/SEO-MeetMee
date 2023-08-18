import os
import requests

def findCoordinates(location):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = os.getenv('Geo_key') # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'q':location} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    #print(data)

    #Acquiring the latitude and longitude from JSON 
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    
    return (latitude,longitude)

#Flask code 
#print(findCoordinates('kenya'))
