import urllib
import json

serviceurl = 'server  adress with some sorce code'          #eg. 'http://python-data.dr-chuck.net/geojson?'

address = input('Enter location:')
url = serviceurl + urllib.urlencode({'sensor':'false','address':address})           #in accordance with above eg. sensor :false
print ('Retrieving:',url)
html = urllib.urlopen(url)
data = html.read()
print ('Retrieved',len(data),'characters')

try: js = json.loads(str(data))
except: js = None

if 'status' not in js or js['status'] != 'OK':
    print ('==== Failure To Retrieve ====')
results = js['results']

print (results[0]['place_id'])
