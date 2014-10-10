import urllib
import urllib2
import sys
import json

test_data = {'op': 'query', 'id': '{\"phone\" : \"13301064170\"}'}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "http://127.0.0.1:7080/socket.io/1/"

req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print str(res)
