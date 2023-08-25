# SWEA 5356 의석이의 세로로 말해요

T = int(input())

for test in range(1, T+1):
    str_list = []
    max_len = 0
    for _ in range(5):
        line = input()
        str_list.append(list(line))
        max_len = max(max_len, len(line))

    for line in str_list:
        if len(line) < max_len:
            line.extend([None] * (max_len-len(line)))

    result = ''
    for line in list(zip(*str_list)):
        for s in line:
            if s != None:
                result += s

    print(f'#{test} {result}')


# 2nd try

T = int(input())

for test in range(1, T+1):
    str_arr = [[''] * 15 for _ in range(5)] # 미리 2차원 배열 만들기
    max_len = 0
    for row in range(5):
        my_str = list(input())
        n = len(my_str)
        max_len = max(n, max_len)
        str_arr[row][:n] = my_str

    result = ''
    for col in range(max_len):
        for row in range(5):
            result += str_arr[row][col]

    print(max_len)
    print(f'#{test} {result}')
