#  how to do WEB CRAWLING IN PYTHON :
# import requests
# from bs4 import BeautifulSoup

# url="http://example.com"

# response=requests.get(url)

# soup=BeautifulSoup(requests.text,"html.parser")
# print(soup.title.text)
# ________________________________________________
# how to do web Crawling in FastAPI 
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app=FastAPI()

@app.get("/news")
def get_news():
    url="https://indianexpress.com/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    title=[]
    for item in soup.find_all("a",class_="article-click topblockNews__sidebarLink"):
        title.append(item.text)
    return{
        "news":title[:2]
    }


