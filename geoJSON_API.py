import urllib.request, urllib.parse, urllib.error
import json

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True :
    address = input("Enter location: ")
    if len(address) < 1 : break

    parms = {}
    parms['key'] = api_key
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving',url)
    data = urllib.request.urlopen(url).read().decode()
    print("Retrieved",len(data),"characters")

    try :
        js = json.loads(data)
    except :
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('==== Failed to retrieve ====')
        print(data)
        continue

    pid = js['results'][0]['place_id']
    print("Place id",pid)
