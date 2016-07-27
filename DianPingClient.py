from bs4 import BeautifulSoup
import HttpClient

def GetTopShopIds():
  res = set([])
  for pIndex in range(1, 50):
    top500Url = "http://dpindex.dianping.com/dpindex?category=10&region=&type=rank&city=1&p=%d" % pIndex 
    res.update([int(idDiv.text) for idDiv in BeautifulSoup(HttpClient.Get(top500Url)).find("div", {"class":"idxmain-subcontainer"}).findAll("div", {"class":"field-index"})])
  return res

