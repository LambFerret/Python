# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:49:46 2021

@author: LambFerret
"""

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
