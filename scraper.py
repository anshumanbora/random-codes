from bs4 import BeautifulSoup
import requests

keywords = ['full stack','full-stack','front end','front-end']
url = "https://news.ycombinator.com/item?id=16967543"
id=1
new_url=url

count_arr=[]

with open('output.txt', 'w+', encoding='utf-8') as file:

    while(True):

        page = requests.get(new_url)
        soup = BeautifulSoup(page.content,'html.parser')
        count = 0

        for span in soup.findAll('span',{'class':'c00'}):
            for key in keywords:
                if key in span.text.lower():
                    count+=1
                    # print(span.text)
                    file.write(span.text)
        count_arr.append(count)

        if soup.findAll('a',{'class':'morelink'}):
            id+=1
            print(id,new_url)
            new_url=url+'&p='+str(id)

        else:

            break

print(count_arr)