# SWEA 5432 쇠막대기 개수

T = int(input())

for test in range(1, T+1):
    my_str = input()
    arr = [0] * len(my_str)

    for i in range(len(my_str)):
        if my_str[i] == '(':
            idx += 1
            star
