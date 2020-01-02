import requests
from bs4 import BeautifulSoup
from pathlib import Path
def download_file(url,local_filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

def download_file_safe(url,local_filename):
    is_complete=False
    while(not is_complete):
        try:
            download_file(url,local_filename)
            is_complete=True
        except Exception as e:
            print(e)
            print("retry %s to  %s"%(url,local_filename))


def download_books(text,base):
    Path("./books/%s"%text).mkdir(parents=True, exist_ok=True)
    search_url="so.php?sokeytm=%s&ka=100&submit="%text
    resp = requests.get(base+search_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    div=soup.find_all("div",class_="info_cate clearfix",id="a1")
    links=[link for link in div[0].find_all("a") if text in  link.text]
    for link in links:
        soup=BeautifulSoup(requests.get(base+link.attrs["href"]).text,"html.parser")
        dd=soup.find_all("dd",style="width:700px;")
        a=dd[0].find_all("a")[0]
        book_url=a.attrs["href"]
        book_file_name="./books/%s/%s.pdf"%(text,a.text.split("/")[0])
        print("download %s to %s" %(book_url,book_file_name))
        download_file_safe(book_url,book_file_name)

base="http://www.guoxuedashi.com/"
text="中国古典文学理论批评专着选辑"
download_books(text,base)
