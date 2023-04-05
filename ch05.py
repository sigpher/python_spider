# from urllib import request, parse
# url = 'https://httpbin.org/post'
# user = {
#     'name': 'choi',
#     'age': 30,
#     'address': 'jiangmen'
# }
# headers = {
#     # 'User-Agent': "Mozilla/5.0 (Windows NT)",
#     'Host': 'httpbin.org',
# }
# data = bytes(parse.urlencode(user), encoding='utf-8')
# req = request.Request(
#     url=url, data=data, headers=headers, method="POST")
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT)')

# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))


# ------------------------------------------------------------------------------------------
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError

# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# ------------------------------------------------------------------------------------------

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://httpbin.org/')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
