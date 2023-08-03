# SWEA 2001 파리퇴치 -> 중요 중요
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.

T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N):
        for j in range(N):
            fly_sum = 0
            for di in range(M):
                for dj in range(M):
                    ni = i + di
                    nj = j + dj
                    if (0 <= ni < N) and (0 <= nj < N):
                        fly_sum += arr[ni][nj]

            if max_val < fly_sum:
                max_val = fly_sum

    print(f'#{test} {max_val}')

"""
강사님 코드 => if (0 <= ni < N) and (0 <= nj < N): 반복문에서 범위 설정을 함으로써, 이 조건문이 안 들어가도 됨.

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())

    lst = []

    for i in range(N):
        lst.append(list(map(int,input().split())))


    MAX = 0


    for i in range(N - M + 1): 
        for j in range(N - M + 1):
            SUM = 0
            for x in range(M):
                for y in range(M):
                    SUM += lst[x+i][y+j]

            if MAX < SUM:
                MAX = SUM

    print(f'#{t} {MAX}')
"""