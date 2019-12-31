
import requests
from bs4 import BeautifulSoup

def dowload_page(base,current):
    url=base+current
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    content=soup.find_all("div",class_="info_txt clearfix")
    links_div=soup.find_all("div",class_="info_cate clearfix")
    links=links_div[0].find_all("a")
    return  content[0].text,links

def download_book(base,first,output_file):
    current=first
    is_first=True
    while(True):
        print(current)
        result=dowload_page(base,current)
        if(is_first):
            tag="w"
        else:
            tag="a"
        with open(output_file, tag) as myfile:
            myfile.write(result[0])
        if(is_first):
            current=result[1][0].attrs["href"]
            is_first=False
            print("first")
        else:
            if(len(result[1])==1):
                break
            else:
                current=result[1][1].attrs["href"]
        
    




base="http://www.guoxuedashi.com/a/1874pgqt/"
first="111871c.html"
output_file="./txt/红楼梦脂评汇校本.txt"
base="http://www.guoxuedashi.com/a/1870a/"
first="114628i.html"
output_file="./txt/汇评金玉红楼梦.txt"

download_book(base,first,output_file)
