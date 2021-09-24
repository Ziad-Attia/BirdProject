import grequests

urls = ['http://www.google.com/finance','http://finance.yahoo.com/','http://www.bloomberg.com/']

def print_url(r, *args, **kwargs):
    fullurl = r.url
    date=
    print(r.url)

def async(url_list):
    sites = []
    for u in url_list:
        rs = grequests.get(u, hooks=dict(response=print_url))
        sites.append(rs)
    return grequests.map(sites)

