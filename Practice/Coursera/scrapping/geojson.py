import urllib.request,urllib.parse
import json
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
while True:
    address = input('Enter- ')
    if len(address)<1: break
    store = dict()
    store['address'] = address
    store['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(store)
    fh = urllib.request.urlopen(url)
    data = fh.read().decode()
    js = json.loads(data)
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(js["results"][0]["place_id"])
    # print(json.dumps(js, indent=4))
