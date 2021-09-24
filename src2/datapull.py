import pandas as pd
import os
import datetime
import getdates as gd
import json
import requests

def get_full_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    dates = gd.get_time_range_list(start, end)
    return dates

def param_format(start, end, apikey):
    params = '/observations/historical.json?&apiKey={}' \
        '&units=e' \
        '&startDate={}&endDate={}'.format(apikey, start, end)
    return params

def geo_format(geocode):
    latitude,longitude = geocode.split(',')
    geofmt = 'https://api.weather.com/v1/geocode/{}/{}'.format(latitude,longitude)
    return geofmt

def geo_req(date, geo):
    apikey = 'e1f10a1e78da46f5b10a1e78da96f525'
    geofmt = geo_format(geo)
    paramfmt = param_format(start=date[0],
            end=date[1],
            apikey=apikey
            )
    req = geofmt + paramfmt
    #print(req)
    return req

def get_all_data(locgeolist, citynum, hemisphere):
    dates = get_full_dates()
    ddict = {}
    for geocode in locgeolist:
        print('getting data for: ' + geocode)
        ddict[geocode] = []
        for date in dates:
            dictinfo = geo_req(date, geocode)
            js = requests.get(dictinfo).json()
            dir = 'data/' + hemisphere + '/city' + str(citynum) + '/_' + geocode
            try:
                os.makedirs(dir)
            except:
                pass
            with open(dir +'/' + str(date[0]) + '-' + str(date[1]) + ".json", 'w') as data_file:
                json.dump(js, data_file)
                data_file.close()
    return

def convertTuple(tup):
    return str(tup[0]) + ',' + str(tup[1])

def pull_data(df, hemisphere):
    latlist = []
    longlist = []
    for col in df.columns: #type: ignore
        if "Latitude" in str(col):
            latlist.append(col)     
        if "Longitude" in str(col):
            longlist.append(col)

    for i in range(2, 7):
        latstr = "City"+str(i)+"Latitude"
        longstr = "City"+str(i)+"Longitude"
        geolist = list(zip(df[latstr], df[longstr])) #type: ignore
        liststrgeo = []
        for tup in geolist:
            liststrgeo.append(convertTuple(tup))
        get_all_data(liststrgeo, i, hemisphere)

northdf = pd.DataFrame(pd.read_csv("geoNorth.csv"))
southdf = pd.DataFrame(pd.read_csv("geoSouth.csv"))

counter = 0
pull_data(southdf, hemisphere='south')
    
#geolist = list(zip(northdf.City2Latitude, northdf.City2Longitude))

#print(liststrgeo)
#print(geolist)

geolist = []
dflist = []
# for lat,long in zip(latlist, longlist):
#     print()
#     print(dflist['geo'])
#    dflist.append(northdf[[lat, long]]) #type: ignore

#    dflist.append(northdf[lat, long])
#    geolist.append((lat,long))

#print(dflist[0])
