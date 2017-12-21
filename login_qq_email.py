import urllib.request
import urllib.parse

url = 'https://rl.mail.qq.com/cgi-bin/getinvestigate?sid=isQUvPa5x_jTbF0H'
postdata = urllib.parse.urlencode({'u':'825182798', 'p':'00000000.whb'}).encode('utf-8')

req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36')

f = urllib.request.urlopen(req)
data = f.read()

print('Status:', f.status, f.reason)
print(data)
fhandle = open('1.html', 'wb')
fhandle.write(data)
fhandle.close()