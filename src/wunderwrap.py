import requests
import json
import time


class WunderWrapper:
    def __init__(self, apikey=None):
        self.apikey ='e1f10a1e78da46f5b10a1e78da96f525' #default until autogen code
        print(self.apikey)
        if apikey is not None:
            self.apikey=apikey
        self.build_call_strings()
    def build_call_strings(self):
        self.prefix = 'https://api.weather.com'
        self.locationstrings = [self.prefix + '/v1/location/', 'no v2 string', self.prefix + '/v3/location/']
        pass
    def jsprint(self, jsondata):
        print(json.dumps(jsondata, indent=4, sort_keys=True))

    def timeconv(self, timestr):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestr)))
    def something(self): #not really sure what this is
        req='NZAA:9:NZ/almanac/daily.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&start=0610'
        return requests.get(req)
    
    def geosearch(self):
        req = 'https://api.weather.com/v1/geocode/34.063/-84.217/observations.json?language=en-US&units=e&startDate=20140615&endDate=20140704&apiKey='+self.apikey
        return requests.get(req)

    def getobservations(self, jsondata):
        return jsondata['observations']

    def getobskeys(self, observations):
        return observations[0].keys()

    def printjsonkeys(self, jsondata):
        keylist=self.getobskeys(self.getobservations(jsondata))
        for key in keylist:
            print(key)

    def get_stations_near_coord(self, longitude, latitude):
        req = 'https://api.weather.com/v3/location/near?geocode=' + longitude + ',' + latitude + '&product=observation&format=json&apiKey=' + self.apikey
        return requests.get(req)

    def get_stations_near_geo(self, geo):
        req = 'https://api.weather.com/v3/location/near?geocode=' + geo + '&product=observation&format=json&apiKey=' + self.apikey
        return requests.get(req).json()

    def get_pws_near_geo(self, geo):
        req = 'https://api.weather.com/v3/location/near?geocode=' + geo + '&product=pws&format=json&apiKey=' + self.apikey
        return requests.get(req).json()


    def stationdaily(self, sloc,start,end=None):
        req= 'https://api.weather.com/v2/pws/history/all/?stationId=' + sloc \
                + '&apiKey=' + self.apikey  \
                + '&units=e'              \
                '&date='+start
        print(req)
        if end is not None:
            req = req+'&endDate='+end
        return requests.get(req)





#respjson = resp.json()
#observations = respjson['observations']
#print(observations.keys())
#for obs in observations:
#    print(timeconv(entry['expire_time_gmt']))




#datenum=respjson['observations'][0]['expire_time_gmt']


#print(datenum)
#print(timeconv(datenum))











"""
    def locsearch(self, sterm):
        req=self.locationstrings[3] \
            'apiKey=' + self.apikey + \
            '&language=en-US' \
            '&query=' + sterm + \
            '&locationType=city,airport,postCode,pws&format=json'
        return requests.get(req)
"""
"""
def stationdaily(self, sloc,start,end=None):
        req= self.prefix \
                self.locationstrings[0]+sloc + \
                '/observations/historical.json?' \
                'apiKey=' + self.apikey +  \
                '&units=e'              \
                '&startDate='+start
        if end is not None:
            req = req+'&endDate='+end
        return requests.get(req)


"""





#resp=requests.get(req)
#resp = locsearch('auck')
#resp=stationdaily('NZAA:9:NZ','20110615')
#resp=something()
#resp = requests.get('https://api.weather.com/v3/dateTime?apiKey=e1f10a1e78da46f5b10a1e78da96f525&geocode=-37.01,174.78&format=json')



#NZAA:9:NZ sloc example
#Start/End Ex (current year): 0610=JUN 10TH
#Start/End Ex: 20110615=JUN 15TH 2011
#https://api.weather.com/v1/location/NZAA:9:NZ/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&startDate=20110615&endDate=20110615

