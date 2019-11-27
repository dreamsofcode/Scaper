from bs4 import BeautifulSoup
import requests
 
page_link = '' #url
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
 
textContent = []
count = len(page_content.find_all("p"))

for i in range(0, count):
    paragraphs = page_content.find_all("p")[i].text
    textContent.append(paragraphs)
   
for i in textContent:
    print(i+"\n")
  
