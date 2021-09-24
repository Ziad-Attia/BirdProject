import requests
req = requests.get('https://api.weather.com/v1/location/30075:4:US/observations/historical.json?&apiKey=e1f10a1e78da46f5b10ae78da96f525&units=e&startDate=150101&endDate=150131')
req = requests.get('https://api.weather.com/v1/location/KONT:9:US/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&startDate=20150701&endDate=20150731')
print(req)
