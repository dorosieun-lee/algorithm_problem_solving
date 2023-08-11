# SWEA 1946 간단한 압축 풀기

# 첫 시도
T = int(input())

for test in range(1, T+1):
    N = int(input())
    my_str = ''
    total = 0
    for _ in range(N):
        char, num = input().split()
        my_str += char * int(num)
        total += int(num)

    n_row = total//10 + 1
    str_arr = [[0] * 10 for _ in range(n_row)]

    for i in range(n_row):
        for j in range(10):
            n = 10 * i + j
            if n >= total:
                break
            str_arr[i][j] = my_str[n]

    print(f'#{test}')
    for line in str_arr:
        result = ''
        for s in line:
            if s != 0:
                result += s
        print(result)


# 다른 풀이
for test in range(1, int(input())+1):
    my_str = ''
    for _ in range(int(input())):
        char, num = input().split()
        my_str += char * int(num)

    print(f'#{test}')
    for i in range(len(my_str)):
        if i%10 == 0 and i != 0: print(f'\n{my_str[i]}', end='')
        else: print(my_str[i], end='')
    print()