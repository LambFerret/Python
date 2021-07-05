def fib_tab(n):
    fib_list = [0, 1, 1]
    if n < 3:
        return 1
    for a in range(3, n+1):
        total = fib_list[a-2] + fib_list[a-1]
        fib_list.append(total)
    return fib_list[n]
    # 코드를 작성하세요.


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))