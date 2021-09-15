from numpy import NAN
import pandas as pd
import re
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

data = pd.read_excel('D:/bird data/Bird_Ranges_AGJ edits.xlsx')
addressesNorth  = pd.DataFrame(columns = ["Bird", "City1", "City2", "City3", "City4", "City5", "City6"])
addressesSouth  = pd.DataFrame(columns = ["Bird", "City1", "City2", "City3", "City4", "City5", "City6"])

geoNorth  = pd.DataFrame(columns = ["Bird", "City1-Latitude ", "City1-Longitude", "City2-Latitude ", "City2-Longitude", "City3-Latitude ", "City3-Longitude", "City4-Latitude ", "City4-Longitude", "City5-Latitude ", "City5-Longitude", "City6-Latitude ", "City6-Longitude"])
geoSouth  = pd.DataFrame(columns = ["Bird", "City1-Latitude ", "City1-Longitude", "City2-Latitude ", "City2-Longitude", "City3-Latitude ", "City3-Longitude", "City4-Latitude ", "City4-Longitude", "City5-Latitude ", "City5-Longitude", "City6-Latitude ", "City6-Longitude"])

pattern = re.compile("^\(.*\)$")
matched = re.match("^\(.*\)$", "(CA)")
is_match = bool(matched)


addressesNorth["Bird"] = data["Species scientific name"]
addressesSouth["Bird"] = data["Species scientific name"]
for ind in data.index:
    num = 1
    StateOrCountry = ""
    if not isinstance(data["Northern Most"][ind], str):
        birdLocNorth = []
    else:
        birdLocNorth = data["Northern Most"][ind].split(", ")
    pattern = re.compile("^\(.*\)$")
    for i in range(len(birdLocNorth)):
        loc = birdLocNorth[-1-i]
        matched = re.match(pattern, loc)
        if(bool(matched)):
            StateOrCountry = loc
        else:
            addressesNorth["City"+str(num)][ind] = loc+", "+StateOrCountry[1:-1]
            num+=1
    num = 1
    StateOrCountry = ""
    
    if not isinstance(data["Southern Most"][ind], str):
        birdLocSouth = []
    else:
        birdLocSouth = data["Southern Most"][ind].split(", ")
    for i in range(len(birdLocSouth)):
        loc = birdLocSouth[-1-i]
        matched = re.match(pattern, loc)
        if(bool(matched)):
            StateOrCountry = loc
        else:
            addressesSouth["City"+str(num)][ind] = loc+", "+StateOrCountry[1:-1]
            num+=1
        

geoNorth  = pd.DataFrame()
geoSouth  = pd.DataFrame()
geoNorth["Bird"] = addressesNorth["Bird"]
geoSouth["Bird"] = addressesSouth["Bird"]

locator = Nominatim(user_agent="smy-application")
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
for i in range(1,7):
    addressesNorth['location'+str(i)] = addressesNorth['City'+str(i)].apply(geocode)
    addressesSouth['location'+str(i)] = addressesSouth['City'+str(i)].apply(geocode)
    geoNorth['City'+str(i)+"-Latitude"] = addressesNorth['location'+str(i)].apply(lambda loc: loc.point.latitude if loc else None)
    geoNorth['City'+str(i)+"-Longitude"] = addressesNorth['location'+str(i)].apply(lambda loc: loc.point.longitude if loc else None)
    geoSouth['City'+str(i)+"-Latitude"] = addressesSouth['location'+str(i)].apply(lambda loc: loc.point.latitude if loc else None)
    geoSouth['City'+str(i)+"-Longitude"] = addressesSouth['location'+str(i)].apply(lambda loc: loc.point.longitude if loc else None)
geoNorth.to_csv('D:/bird data/geoNorth.csv')
geoSouth.to_csv('D:/bird data/geoSouth.csv')
addressesNorth.to_csv('D:/bird data/addressesNorth.csv')
addressesSouth.to_csv('D:/bird data/addressesSouth.csv')