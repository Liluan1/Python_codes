import requests

def geocode(address):
    parameters = {'address': address, 'output': 'xml', 'ak': '5Ee1glQ0PwgQcDmZgMF9mi6XYgTVV5Ei'}
    base = 'http://api.map.baidu.com/geocoder/v2/'
    response = requests.get(base, params=parameters)
    answer = response
    print(answer.text)

if __name__ == '__main__':
    geocode('北京市海淀区上地十街10号')
