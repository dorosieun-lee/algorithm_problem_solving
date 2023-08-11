# SWEA 9489 고대 유적
# NxM 행렬임에 주의

T = int(input())

for test in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)] # NxM array, 0,1로 이루어짐

    max_length = 0
    for i in range(N):
        row_len = 0
        for j in range(M):
            if arr[i][j] == 1:
                row_len += 1
            elif arr[i][j] == 0:
                max_length = max(max_length, row_len)
                row_len = 0

        max_length = max(max_length, row_len)

    for j in range(M):
        col_len = 0
        for i in range(N):
            if arr[i][j] == 1:
                col_len += 1
            elif arr[i][j] == 0:
                max_length = max(max_length, col_len)
                col_len = 0

        max_length = max(max_length, col_len)

    print(f'#{test} {max_length}')