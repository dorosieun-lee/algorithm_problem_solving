'''
문제구상
1. dfs로 모든 경로 탐색
2. input 문자열 자체를 visited 2차원 배열로 사용 하기
'''


def dfs(i, j, Arr):
    if Arr[i][j] == 3:
        return 1

    else:
        Arr[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and Arr[ni][nj] != 1:
                if dfs(ni, nj, Arr):
                    return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                result = dfs(i, j, miro)

    print(f'#{test_case} {result}')

