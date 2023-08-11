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