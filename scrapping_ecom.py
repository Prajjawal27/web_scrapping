import requests
import time
from bs4 import BeautifulSoup
import pandas as pd 
product_name=[]
price=[]
description=[]
rating=[]

# for i in range(2,10):
    
url="https://www.flipkart.com/search?q=mobile+phone+under+20000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_19_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_19_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobile+phone+under+20000&requestId=4eab32df-3e5a-462b-94b3-d5411fac9463&as-searchtext=mobile%20phone%20under%20="
r= requests.get(url)
# print(r)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("div",class_="_4rR01T")
for i in names:
    name=i.text
    product_name.append(name)
# print(product_name)

prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
for j in prices:
    rate=j.text
    price.append(rate)
# print(price)

desc=soup.find_all("ul",class_="_1xgFaf")
for k in desc:
    descri=k.text
    description.append(descri)
# print(description)

ratin=soup.find_all("div",class_="_3LWZlK")
for x in ratin:
    rati=x.text
    rating.append(rati)
df= pd.DataFrame({"Product_name":product_name,"Prices":price,"descrription":description,"Rating":rating})
df.to_csv("flipkart_mobiles.csv")
# print(rating)
# print(names)
# print(soup)
    # np=soup.find("a" , class_="_1LKTO3").get("href")
    # cnp="https://www.flipkart.com"+np
    # print(cnp)
# url=cnp
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"lxml")
# print(soup)

