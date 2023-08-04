# SWEA 16910 원 안의 점

T = int(input())

for test in range(1, T+1):
    N = int(input()) # 반지름
    cnt = 0
    for x in range(N*(-1), N+1):
        for y in range(N*(-1), N+1):
            if x**2 + y**2 <= N**2:
                cnt += 1

    print(f'#{test} {cnt}')

