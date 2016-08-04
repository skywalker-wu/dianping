from bs4 import BeautifulSoup
import HttpClient
import re
import AzureStorage

name="dianping"
key="/J3rUIw92KxHbgkyrlSg1ii4dH954IjEPSiK6bK0QtLKuuodMADinBDWrxOaMi5OiD4jRwQIiyjS6DYUAYOyPg=="
AzureStorage.Init(name, key)
AzureStorage.EnsureTable("topshops")

def GetTopShops(city):
  ret = []

  topUrlTemplete="http://dpindex.dianping.com/dpindex?category=10&region=&type=rank&city=%d&p=%d"
  for pIndex in range(1, 51):
    ret += ParseShopInfo(HttpClient.Get(topUrlTemplete % (city, pIndex)))
  for shop in ret:
    shop["city"]=city
  return ret

def ParseShopInfo(text):
  ret = []
  bsObj = BeautifulSoup(text)
  
  for li in bsObj.findAll("li", {"class":re.compile("rank-item")}): 
    href = li.find("a")["href"]
    id = int(re.search("\d+", href).group())
    name = li.find("div", {"class":"field-name"}).text
    rank = int(li.find("span", {"class":"ranknum"}).text)
    ret.append({"id":id, "href":href, "name":name, "rank":rank})

  return ret

def UpdateShop(shop):
  AzureStorage.Update(shop['city'], '%d_%d' % (shop["city"], shop['rank']), shop)

def ListShops(city):
  for entity in AzureStorage.Query("PartitionKey eq '%d'" % city):
    id = entity["id"]
    href = entity["href"]
    name = entity["name"]
    rank = entity["rank"]
    city = entity["city"]
    yield {"id":id, "href":href, "name":name, "rank":rank, "city":city}

