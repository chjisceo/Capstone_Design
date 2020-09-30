import urllib.request
import urllib.parse


pageNo = 1
url = 'http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo'
queryParams = ('?' + 'ServiceKey' + '=11PtzPKFz%2F8XXCD0NO7lxl7%2Fb7VDNEFtTpbcvYi2vzDBicQpPAz5o7auO3VtzGUZcfibeIh0aWgRVOeoL6I06A%3D%3D' + (urllib.parse.quote_plus('&pageNo={}'.format(pageNo)) + '&pageSize' + '1000&')


request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read()
print (response_body)
