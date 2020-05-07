from bs4 import BeautifulSoup
import requests
import json
import time
data = []


def onlineKhabarNews(x=15):
    '''Gives fresh onlineKhabarNews from internet while parameter x is in which
    you get to chose how many small headlines you want. It will get you a main
    main headline with summery, link to news and other headlines with link'''

    oKhabar = requests.get('https://www.onlinekhabar.com/').text
    onlineKhabarSoup = BeautifulSoup(oKhabar, 'lxml')

    mainNews = onlineKhabarSoup.find_all('h2', class_='highlight')
    for mainN in mainNews:
        news1_h = mainN.a.text
        news1_a = mainN.a.get('href')
        news1_p = paragraphOnlineKhabar(news1_a)
        data.append({'source': 'onlinekhabar', 'headline': news1_h, 'summary': news1_p, 'newsLink': news1_a})
    n = 0
    for oH in onlineKhabarSoup.find_all('h2', class_='post__title'):

        oH_p = paragraphOnlineKhabar(oH.a.get('href'))
        data.append({'source': 'onlinekhabar', 'headline': oH.text, 'summary': oH_p, 'newsLink': oH.a.get('href')})
        n += 1
        if n > x:  # x is parameter
            break


def ekantipurNews():
    '''Gives fresh and realtime ekantipur from internet
    using BeautifulSoup  '''
    e_kantipur = requests.get('https://www.ekantipur.com/').text
    ekantipurSoup = BeautifulSoup(e_kantipur, 'lxml')

    for mainN in ekantipurSoup.find_all('h1'):
        if mainN.a is not None:
            data.append({'source': 'ekantipur', 'headline': mainN.a.text, 'summary': '', 'newsLink': mainN.a.get('href')})
    extraNews = ekantipurSoup.find('div', class_='more-main-news').find_all('article')
    for otherN in extraNews:
        data.append({'source': 'ekantipur', 'headline': otherN.a.text,
             'summary': otherN.p.text, 'newsLink': otherN.a.get('href')})


def paragraphOnlineKhabar(link):
    a = requests.get(link)
    para = ''
    a.encoding = 'UTF-8'
    a = a.text
    b = BeautifulSoup(a, 'lxml')
    m = b.find_all('p')
    for x in range(0, 2):
        para = para + m[x].text
    return para


def newsToJson():
    '''
    This function will return news in json format and will get news from other
    sources like ekantipur and hence dump all the data into json file
     '''
    onlineKhabarNews()
    ekantipurNews()
    with open('newsNep.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=1)
    print(type(data))
    print(data)
    return data


if __name__ == '__main__':
    while True:
        newsToJson()
        time.sleep(60*60)
