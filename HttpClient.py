import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0',}
session = requests.Session()

def Get(url):
  req = session.get(url, headers=headers)
  return req.text


