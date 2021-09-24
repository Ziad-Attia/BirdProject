import wunderwrap as wr
import json


wrap = wr.WunderWrapper()

f = open('../apisave/geosearchpws.json')
data = json.loads(f.read())


for loc in data['locations']:
    try:
        print(loc['result']['location']['stationId'])
    except:
        print(loc['result'])
        continue

    #print(data[key])
