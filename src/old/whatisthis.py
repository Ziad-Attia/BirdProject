import pandas as pd
import wunderwrap

wr = wunderwrap.WunderWrapper()

data = pd.DataFrame(pd.read_csv('locations.csv'))
data['Geocode'] = data.Longitude.astype(str) + ',' + data.Latitude.astype(str) #type: ignore

print(data[data.duplicated(['Geocode'])])
for index, row in data.iterrows():
    #print(row['Actual'], row['Geocode'])
    pass
#locationset = len(set(data['Actual'].unique())) #type: ignore
#locationset = len(set(data['Geocode'].unique())) #type: ignore

#print(locationset)
#print(data)


#loc='NZAA:9:NZ'

#years=['2011', '2011'] #max 31days
#months=['06','06']
#days=['14','15']
#start=years[0]+months[0]+days[0]
#end=years[1]+months[1]+days[1]

#respjson=wr.stationdaily(loc,start,end).json()
#respjson=wr.geosearch().json()
#print(respjson)

#obslist=wr.getobservations(respjson)
#wr.printjsonkeys(respjson)
#df=pd.json_normalize(obslist)#.dropna(axis=1)

#dates = ['expire_time_gmt', 'valid_time_gmt']
#df[dates]=(df[dates]).apply(pd.to_datetime, unit='s')
#print(df)
#dfobs = dfobs.append(dfItem, ignore_index=True)    

#df[dates]=df[dates].apply(lambda t: wr.timeconv(t))
# def buildframe(obslist): 
#     dfobs = pd.DataFrame()  
#     for item in obslist:
#         dfItem = jsonToDataFrame(obslist)                
#         dfobs = dfobs.append(dfItem, ignore_index=True)    
#    return dfobs

