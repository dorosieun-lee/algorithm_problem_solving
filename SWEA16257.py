# SWEA 16257 색칠하기
T = int(input())

for test in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    # color는 두가지 뿐

    arr = [[0]*10 for _ in range(10)] # 0으로 가득 찬 array 생성

    for n in range(N):
        for i in range(data[n][0], data[n][2]+1):
            for j in range(data[n][1], data[n][3]+1):
                if (data[n][-1] == 1) and (arr[i][j] != 1):
                    arr[i][j] += 1
                if (data[n][-1] == 2) and (arr[i][j] != 2):
                    arr[i][j] += 2

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{test} {cnt}')