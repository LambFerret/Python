def max_profit_memo(price_list, count, cache):
    if count <= 1:
        cache[count] = price_list[count]
        return price_list[count]
    if count in cache:
        return cache[count]
    else:
        lists = 0 
        for a in range(1, count//2):
            
            lists.append(cache[a] + cache[count - a])
            return max(lists)
    # 코드를 작성하세요.

    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


