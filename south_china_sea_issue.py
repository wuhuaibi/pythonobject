import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

while True:
    print ''
    que = raw_input('Enter the question you want to find:')
    if ( len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'q': que, 'count': '10'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read()
    headers = connection.info().dict
    print 'Remaining', headers['x-response-time']
    js = json.loads(data)
    print json.dumps(js, indent=4)

    for u in js['statuses'] :
        s = u['user']['entities']['screen_name']
        print 'screen_name:', s
        print 'test:', u['test']