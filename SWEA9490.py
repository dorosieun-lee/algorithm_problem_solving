# SWEA 9490 풍선팡
T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_val = 0
    for i in range(N):
        for j in range(M):
            pollen_sum = arr[i][j] # 자기자신
            num = arr[i][j]
            for k in range(4):
                for p in range(1, num+1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if (0 <= ni < N) and (0 <= nj < M):
                        #print(ni, nj, arr[ni][nj])
                        pollen_sum += arr[ni][nj]
            #print(f'\n {pollen_sum}\n')
            if max_val < pollen_sum:
                max_val = pollen_sum

    print(f'#{test} {max_val}')
