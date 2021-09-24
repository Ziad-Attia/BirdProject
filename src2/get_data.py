import getdates as gd
from pathlib import Path
import os
import requests
import json
import datetime
from uniquify import uniquify as unq
import grequests
#https://api.weather.com/v1/geocode/34.063/-84.217/observations.json?language=en-US&units=e&startDate=20140615&endDate=20140704&apiKey=yourApiKey
#https://api.weather.com/v1/location/30075:4:US/observations.json?language=en-US&units=estartDate=20140615&endDate=20140704&apiKey=yourApiKey

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

def formatreq(geocode, date):
    return geo_req(date, geocode)

def loc_format(loc):
    locfmt = 'https://api.weather.com/v1/location/{}'.format(loc)
    return locfmt

def restore_data():
    file = open('../apisave/geosearchpws.json')
    jsd = json.load(file) 
    return jsd

def get_stationids(jsd):
    stationdict = {}
    #print(jsd['locations'][0]['result']['location']['stationId'])
    for i in range(len(jsd['locations'])):
        location = jsd['locations'][i]
        try:
            stationids = location['result']['location']['stationId']
            geo = location['geocode']
            stationdict[geo] = stationids
            continue
        except:
    #        print('ERROR ' + location['actual'] + ' HAS NO DATA')
            continue
    return stationdict

def get_actualids(jsd):
    stationdict = {}
    for i in range(len(jsd['locations'])):
        location = jsd['locations'][i]
        try:
            actualid = location['actual'].replace(" ", "_")
            actualid = actualid.replace(",", "_")
            actualid = actualid.replace("/n", "")
            geo = location['geocode']
            stationdict[geo] = actualid
            continue
        except:
            #print('ERROR ' + location['actual'] + ' HAS NO DATA')
            continue
    return stationdict


def test(apikey, date, loc):
    locfmt = loc_format(loc)
    paramfmt = param_format(start=date[0],
            end=date[1],
            apikey=apikey
            )
    req = locfmt + paramfmt
    #print(req)
    #print(requests.get(req))

def get_full_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    dates = gd.get_time_range_list(start, end)
    return dates

#    ret = requests.get(req).json()
#    print(ret)
#    return ret
    #return json.loads(ret.json())
    #try:
    #except:
    #    return ({'error': 'error'})

def get_all_data(locgeolist):
    dates = get_full_dates()
    ddict = {}
    for geocode in locgeolist:
        ddict[geocode] = []
        for date in dates:
            dictinfo = geo_req(date, geocode)
            dateval = date[0] + '-' + date[1]
            ddict[geocode].append({dateval: dictinfo})
        with open('_'+geocode, 'w') as data_file:
            data_file.write(json.dumps(ddict))
            data_file.close()
    return


def write_all_reqs(locgeolist):
    dates = get_full_dates()
    reqlist = []
    for geocode in locgeolist:
        actual = actualdict[geocode]
        for date in dates:
            req = geo_req(date, geocode)
            reqlist.append(req)
        writepath = Path('reqlists/_' + geocode + '.txt')
        mode = 'a+' if os.path.exists(writepath) else 'w+'
        with open(writepath, mode) as f:
            for req in reqlist:
                f.write('%s\n' % req) 
            f.close()
    return
def read_all_reqs(dir):
    reqdict = {}
    for reqlist in os.listdir(dir):
        with open(dir+'/'+reqlist, 'r') as f:
            reqs = [line.rstrip() for line in f]
            #print(reqs)
        reqdict[reqlist] = reqs
    return reqdict

apikey = 'e1f10a1e78da46f5b10a1e78da96f525'
jsd = restore_data()
actualdict = get_actualids(jsd)
#print(actualdict)
print(len(list(set(actualdict.keys()))))
locgeolist = list(actualdict.keys())
locgeodict = {}
actuals = []


dates = get_full_dates()
responses = get_reqs_for_geo(locgeolist[0], dates)
counter = 0
def get_reqs_for_geo(geocode, dates): 
    with requests.Session() as session:
        for date in dates:
            try:
                response = geo_req(date, geocode)
                parsed_response = response.json()
                print(f"Response: {json.dumps(parsed_response, indent=2)}")
            except Exception as err:
                print(f"Exception occured: {err}")
                pass


for response in responses:
    writepath = Path('responses/_' + str(counter) + '.json')
    mode = 'a+' if os.path.exists(writepath) else 'w+'
    with open(writepath, mode) as f:
        json.dump(response.json(), f)
        f.close()
    counter = counter + 1
    
#for geo in list(actualdict.keys()):
#    actuals.append(actualdict[geo])
#unq(actuals)
#print(actuals)
#loc = stations[0]
#dates = gd.gen_dates()
#print(locgeolist)
#write_all_reqs(locgeolist)
#test(apikey, date, loc)
#reqdict = read_all_reqs('reqlists')





#https://api.weather.com/v2/pws/history/all?stationId=INHULU1&format=json&units=e&date=20180320&numericPrecision=decimal&apiKey=e1f10a1e78da46f5b10a1e78da96f525


