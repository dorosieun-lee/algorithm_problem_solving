# SWEA 1289 원재의 메모리 복구하기

T = int(input())
for test in range(1, T+1):
    bit = list(map(int, list(input())))
    N = len(bit)
    init = [0] * N

    start = 0
    target = 1
    cnt = 0
    while True:
        if bit == init:
            break
        cnt += 1
        idx = bit[start:].index(target)
        idx += start
        for i in range(idx, N):
            init[i] = target
        start = idx + 1
        target = 0 if target == 1 else 1

    print(f'#{test} {cnt}')

'''
# 더 간단한 풀이..!
T = int(input())
for test in range(1, T+1):
    bit = list(map(int, list(input())))
    cnt = 0
    past = 0
    for n in bit:
        if past != n:
            past = n
            cnt += 1

    print(f'#{test} {cnt}')
'''