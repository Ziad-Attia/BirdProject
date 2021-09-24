"""
{
        "actual": "no results",
        "geocode": "nan,nan",
        "original": "Shasta, California (southwest of Redding)",
        "result": {
            "failure": " Geocode nan  is not allowed.,  "
            }
        }


{
        "actual": "Cave of Swallows, San Luis Potosi, Mexico",
        "geocode": "21.599683,,-99.09876",
        "original": "Sotano de Las Golondrinas, Mexico",
        "result": {
            "failure": " Geocode 21.600,0.000,-99.09876  is not allowed.,  "
            }
        }


"actual": "no results",
            "geocode": "nan,nan",
            "original": "Southeast of Lake Ghoubet, southwest of We'a, Djibouti",
            "result": {
                    "failure": " Geocode nan  is not allowed.,  "
                    }
            "actual": "no results",
            "geocode": "nan,nan",
            "original": "Telaga, Indonesia, (southwest of Kruing, west of Sebangau National Park",
            "result": {
                "failure": " Geocode nan  is not allowed.,  "
            }

            "actual": "Cannot find",
            "geocode": "nan,nan",
            "original": "Warmuri Trail, Kukama, Guyana",
            "result": {
                "failure": " Geocode nan  is not allowed.,  "
            }


"""
import wunderwrap as wr
wrap = wr.WunderWrapper()
import json
listcodesfixed = ['21.599683,-99.09876','63.960387,-143.6297']

jsonFile = open("../apisave/fix.json", "w")

for code in listcodesfixed:
    result = wrap.get_stations_near_geo(code)
    js = json.dumps(result, sort_keys=True, indent=4)
    print(js)
    jsonFile.write(js)

jsonFile.close()

