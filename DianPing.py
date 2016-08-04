from bs4 import BeautifulSoup
import HttpClient
import re
import AzureStorage

name="dianping"
key="/J3rUIw92KxHbgkyrlSg1ii4dH954IjEPSiK6bK0QtLKuuodMADinBDWrxOaMi5OiD4jRwQIiyjS6DYUAYOyPg=="
AzureStorage.Init(name, key)
AzureStorage.EnsureTable("topshops")

def GetTopShops():
  ret = []

  topUrlTemplete="http://dpindex.dianping.com/dpindex?category=10&region=&type=rank&city=1&p=%d"
  for pIndex in range(1, 51):
    ret += ParseShopInfo(HttpClient.Get(topUrlTemplete % pIndex))

  return ret

def ParseShopInfo(text):
  ret = []
  bsObj = BeautifulSoup(text)
  
  for li in bsObj.findAll("li", {"class":re.compile("rank-item")}): 
    href = li.find("a")["href"]
    id = int(re.search("\d+", href).group())
    name = li.find("div", {"class":"field-name"}).text
    rank = int(li.find("span", {"class":"ranknum"}).text)
    ret.append({"id":id, "href":href, "name":name})

  return ret

def UpdateShop(shop):
  AzureStorage.Update(shop['id'], shop['id'], shop)
