# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:06:04 2021

@author: LambFerret
"""
def min_coin_count(value, coin_list):
    num_coin = 0
    for a in range(len(coin_list)):
        temp = []
        temp.append(value - coin_list[a])
        value = max(temp)
        if value > 0:
            num_coin += 1
            return min_coin_count(value, coin_list)
        else:
            break
    
    # 코드를 작성하세요.

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))