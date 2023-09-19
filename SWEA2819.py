# SWEA 2819 격자판의 숫자 이어 붙이기

# 총 6번 이동하면 7자리 수가 생성됨
# 서로 다른 7자리 수의 개수를 구해라
# 갔던 곳 다시 가도 됨;;; -> visited 필요 없음

def DFS(i, j, my_num):
    if len(my_num) == 7:
        my_set.add(my_num)
        return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N) and (0 <= nj < N): # and not visited[ni][nj]:
            #visited[ni][nj] = True
            DFS(ni, nj, my_num+str(MAP[ni][nj]))


T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for test in range(1, T+1):
    N = 4
    MAP = [list(map(int, input().split())) for _ in range(N)]
    my_set = set()

    for i in range(N):
        for j in range(N):
            #visited = [[False] * N for _ in range(N)]
            #visited[i][j] = True
            DFS(i, j, str(MAP[i][j]))

    result = len(my_set)

    print(f'#{test} {result}')