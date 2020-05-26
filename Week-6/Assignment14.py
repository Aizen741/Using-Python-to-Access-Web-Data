import urllib.request, urllib.parse, urllib.error
import json

counts = list()
while True:
    address = input('Enter location')
    if len(address) < 1:
        break
    print('Retrieving', address)
    connection = urllib.request.urlopen(address)
    data = connection.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)

    except:
        js = None

    comments = js['comments']
    for comment in comments:
        counts.append(comment['count'])
    print('Count', len(comments))
    print('Sum', sum(counts))