# SWEA2005 파스칼의 삼각형

T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] # NxN array 생성

    for i in range(N):
        for j in range(0,i+1):
            if j in [0, i]:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{test}')
    for i in range(N):
        print(*arr[i][:i+1])
