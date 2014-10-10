import urllib
import urllib2
import sys
import json

para = ['name', 'phone', 'gent', 'province', 'city', 'address', 'lesson', 'level', 'price', 'comment'];
test_data = {'op': 'create', 'id':"{\"name\":\"b\", \"phone\":\"c\"}"}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "http://127.0.0.1:7080/socket.io/1/"

req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
