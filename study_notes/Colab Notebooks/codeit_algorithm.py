#1

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

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

#2
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


#3
def course_selection(course_list):
    course_list.sort(key=lambda x: (x[1], x[0]))
    empty_lists = []
    end_time = None
    for every_lists in course_list:
        if course_list[0] == every_lists:
            end_time = every_lists[1]
            empty_lists.append(every_lists)
        elif every_lists[0] > end_time:
            end_time = every_lists[1]
            empty_lists.append(every_lists)
    return empty_lists
    # 코드를 작성하세요.


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
