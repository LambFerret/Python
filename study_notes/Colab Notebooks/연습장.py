# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:28:05 2021

@author: LambFerret
"""

# 여기에 코드를 작성해주세요.
"""
import requests
from bs4 import BeautifulSoup

responce = requests.get('https://workey.codeit.kr/music/index')
soup = BeautifulSoup(responce.text, 'html.parser')

tags = soup.select(".popular__order li")

artist = []
for a in tags:
    artist.append(a.text.strip())
artist
import requests
from bs4 import BeautifulSoup
sources = requests.get('https://workey.codeit.kr/orangebottle/index')
soup = BeautifulSoup(sources.text, 'html.parser')
tags = soup.select(".phoneNum span")

phone_numbers = []
for a in tags:
    phone_numbers.append(a.text.strip())
# 코드를 작성하세요

# 결과 출력
print(phone_numbers)
"""
"""
def func(num1, num2, *args):
    return num1 + num2 + sum(args)

data = [1,2,3,4,5]
func(*data)
"""
import random

lotto = []
while len(lotto) < 6:
    a = random.randint(1, 46)
    if a not in lotto:
        lotto.append(a)
        lotto.sort()


random.randint?
