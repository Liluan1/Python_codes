import http.client
import json
from urllib.parse import quote_plus

base = '/geocoder/v2/'

def geocode(address):
    path = '{}?address={}&output=json&ak=5Ee1glQ0PwgQcDmZgMF9mi6XYgTVV5Ei'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('api.map.baidu.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply)

if __name__ == '__main__':
    geocode('北京市海淀区上地十街10号')
