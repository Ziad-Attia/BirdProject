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

