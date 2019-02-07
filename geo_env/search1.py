import geocoder
if __name__ == '__main__':
    g = geocoder.baidu('北京天安门',key='5Ee1glQ0PwgQcDmZgMF9mi6XYgTVV5Ei')
    print(g.json)
    latlng = [39.915446357113886, 116.40384918664363]
    h = geocoder.baidu(latlng, method='reverse', key='5Ee1glQ0PwgQcDmZgMF9mi6XYgTVV5Ei')
    print(h.json)
