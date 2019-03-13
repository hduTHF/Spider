from bs4 import BeautifulSoup
from spider_tool import get_page,insert_info
from mail import send_mail
import re
import requests
import sys
import pymysql


proxies = { "http": "http://127.0.0.1:1080", }
# def search_freebuf(flag=1):
#     url='http://www.freebuf.com/'
#     html=get_page(url,sflag=flag)
#     print(html)

def search_anquanke(flag=1):

    url='https://www.anquanke.com/'
    html=get_page(url,sflag=flag)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        titles=soup.find_all(class_='title')
        content= soup.find_all(class_='desc hide-in-mobile-device')
        time = soup.find_all(class_='date')
        title_lst=[]
        href_lst=[]
        content_lst=[]
        time_lst=[]
        for tag in titles:
            if tag.a:
                title_lst.append(tag.a.string)
                href_lst.append(url+tag.a['href'][1:])
        for tag in content:
            content_lst.append(tag.string)
        for tag in time:
            time_lst.append(tag.span.text.strip())
        for i in range(0, len(href_lst)):
           insert_info(title=title_lst[i], content=content_lst[i], time=time_lst[i], href=href_lst[i],source='anquanke')
    except Exception as e:
        print(e)


def func(tag):
    return  tag.has_attr('data-datetime')

def search_ipvm(flag=1):
    url='https://ipvm.com/'
    html=get_page(url,sflag=flag)
    try:
        soup=BeautifulSoup(html,'html.parser')
        titles=soup.find_all(class_='title-link-primary')
        time=soup.find_all(func)
        content=soup.find_all(class_='article-snippet text-muted m-b-0 hidden-xs-down')
        content1=soup.find_all(class_='article-snippet text-muted hidden-sm-down')
        #print(desc1)
        time_lst = []
        href_lst = []
        title_lst = []
        content_lst = []
        content_lst.append(content1[0].string)
        for tag in titles:
            title_lst.append(tag.string)
            href_lst.append(tag['href'])
        for tag in time:
            time_lst.append(tag['data-datetime'])
        for tag in content:
            content_lst.append(tag.string)

        for i in range(0,len(href_lst)):
            insert_info(title=title_lst[i],content=content_lst[i],time=time_lst[i],href=href_lst[i],source="ipvm")
    except Exception as a:
        print(a)

def hik(flag=1):
    url='http://www.hikvision.com/cn/support_list_591.html'
    html=get_page(url,sflag=flag)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        tags=soup.select('li[class="clearfix"]')
        titles=[]
        hrefs=[]
        time=[]
        for tag in tags:
            titles.append(tag.a.string)
            hrefs.append('http://www.hikvision.com/cn/'+tag.a['href'])
            time.append(tag.span.string)
        for i in range(0,len(titles)):
            insert_info(title=titles[i],time=time[i],href=hrefs[i],source="hik")
    except Exception as a:
        print(a)

def yushi(flag=1):
    url='http://cn.uniview.com/Security/Notice/'
    html=get_page(url,sflag=flag)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.select('ul[id="NewsListStyle"]')
        href_lst=[]
        title_lst=[]
        time_lst=[]
        for tag in (tags[0].find_all('a')):
            href_lst.append('http://cn.uniview.com'+tag['href'])
            title_lst.append(tag.string)
            date=tag['href'].split('/')[3][:4]+'-'+tag['href'].split('/')[3][-2:]
            time_lst.append(date)
        for i in range(0,len(title_lst)):
            insert_info(title=title_lst[i],time=time_lst[i],href=href_lst[i],source='uniview')
    except Exception as a:
        print(a)

def cert(flag=1):
    url="http://cert.360.cn"
    html = get_page(url, sflag=flag)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        titles=soup.find_all(class_='news-title')
        date=soup.find_all(class_='news-date')
        content=soup.find_all(class_="news-conent")
        #print(content)
        title_lst=[]
        href_lst=[]
        time_lst=[]
        content_lst=[]
        for tag in titles:
            title_lst.append(tag.a.string)
            href_lst.append(url+tag.a['href'])

        for tag in date:
            time_lst.append(tag.string.split(' ')[1].strip())

        for tag in content:
            content_lst.append(tag.string)

        for i in range(len(title_lst)):

            insert_info(title=title_lst[i],content=content_lst[i],time=time_lst[i],href=href_lst[i],source='360cert')
    except Exception as a:
        pass




if __name__ == '__main__':
    #search_freebuf(1)
    search_anquanke(0)
    #search_ipvm(0)
    hik(0)
    yushi(0)
    cert(0)