# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:22:32 2023

@author: User 2
"""

from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.thedailystar.net/news/world').text
html_text2 = requests.get('https://www.thedailystar.net/sports/cricket').text
html_text3 = requests.get('https://www.thedailystar.net/sports/football').text

soup = BeautifulSoup(html_text, 'lxml')
soup2 = BeautifulSoup(html_text2, 'lxml')
soup3 = BeautifulSoup(html_text3, 'lxml')


title = soup.find_all('h3', class_='title')
title2 = soup2.find_all('h4', class_='title')
title3 = soup3.find_all('h4', class_='title')
print('')
print('WELCOME TO NADEEF NEWS NETWORK')
print('(source: The Daily Star)')
print('')
print("Enter 1 for world-news or 2 for sports-news:")
topic = input()

if(int(topic) == 1):
    for i in range(len(title)):
        print(title[i].text)
        print('')
        print('https://www.thedailystar.net'+title[i].find('a')['href'])
        print("--------------")
    



elif(int(topic) == 2):
    print('')
    print("Enter 3 for cricket-news or 4 for football-news:")
    sport = input()
    if(int(sport) == 3):
        for i in range(len(title2)):
                print(title2[i].text)
                print('')
                print('https://www.thedailystar.net'+title2[i].find('a')['href'])
                print("--------------")
       

    if(int(sport) == 4):
        for i in range(len(title3)):
            print(title3[i].text)
            print('')
            print('https://www.thedailystar.net'+title3[i].find('a')['href'])
            print("--------------")







