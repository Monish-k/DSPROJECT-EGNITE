import requests
import requests
from bs4 import BeautifulSoup
res=requests.get('https://towardsdatascience.com/')
txt=(res.text)
status=(res.status_code)
print(txt,status)

line = f.read()
line = line.split("\n")

for url in line:
    try:
        feeds = search(url)
        print(feeds[0].url)
        fFeed.write(feeds[0].url+"\n")
    except:
        pass

fUrl.close()
fFeed.close()
page_title = soup.title
page_body = soup.body
page_head = soup.head
print(page_title, page_head)
all_h1_tags = []
for element in soup.select('h1'):
    all_h1_tags.append(element.text)
seventh_p_text = soup.select('p')[20].text

print(all_h1_tags, seventh_p_text)
image_data = []
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({"src": src, "alt": alt})

print(image_data)
all_links = []
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)