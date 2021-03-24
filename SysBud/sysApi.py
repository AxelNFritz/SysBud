import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5abcaa1959c745bd85828a4c5ca2f97a',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api-extern.systembolaget.se')
    conn.request("GET", "/site/v1/site/0132/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))