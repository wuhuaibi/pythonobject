# import socket
# import socks
# import requests

# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket
# print (requests.get('https://www.baidu.com/').text)

# import urllib3.contrib.pyopenssl
# urllib3.contrib.pyopenssl.inject_into_urllib3()


import requests

resp = requests.get('https://www.google.com/', proxies=dict(http='socks5://127.0.0.1:1080', https='socks5://127.0.0.1:1080'), verify=False)

print ('success!')

# import socks
# import socket 
# from urllib import request 
# from urllib.error import URLError
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
# socket.socket = socks.socksocket
# try: 
#     response = request.urlopen('https://www.google.com/') 
#     print(response.read().decode('utf-8'))
# except URLError as e: 
#     print(e.reason)

# -*- coding: utf-8 -*-
# import socket
# import socks
# import urllib2
# SOCKS5_PROXY_HOST = '127.0.0.1' 
# SOCKS5_PROXY_PORT = 1080  
# default_socket = socket.socket
# socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT) 
# socket.socket = socks.socksocket


# url = 'https://www.google.com/'
# request = urllib2.Request(url)
# request.add_header("User-Agent", "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101")
# html_source = urllib2.urlopen(request, timeout=10).read()

# if html_source:
#     print 'ok'
# else:
#     print 'fail'


# url = 'https://www.google.com/'
# request = urllib2.Request(url)
# request.add_header("User-Agent", "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101")
# html_source = urllib2.urlopen(request, timeout=10000)

# if html_source:
#     print 'ok'
# else:
#     print 'fail'