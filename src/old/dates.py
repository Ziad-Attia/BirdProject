import pandas as pd

def get_dates():
#    fulldata = pd.DataFrame(pd.read_csv('sheetrel.csv'))
    dframe = pd.DataFrame(pd.read_csv('../data/sheetrel.csv'))
    #dframe['Geocode'] = dframe.Longitude.astype(str) + ',' + dframe.Latitude.astype(str) #type: ignore
    print(dframe.columns)
    northlist = []
    southlist = []
    for col in dframe.columns: #type: ignore
        if col.startswith('n'):
            northlist.append((col, col[1:]))
        else:
            southlist.append((col, col[1:]))
    northdf = pd.DataFrame()
    southdf = pd.DataFrame()
    for tup in northlist:
        northdf[tup[1]] = dframe[tup[0]]
    for tup in southlist:
        southdf[tup[1]] = dframe[tup[0]]
    print(northdf)
    print(southdf)
   
    #for col in dframe.columns:
        #print(dframe[col])
#    listfullcols = list(fulldata.columns)

    #print(locframe)
#    dict_locations = {}


get_dates()
