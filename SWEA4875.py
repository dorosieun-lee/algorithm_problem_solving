# SWEA 4875 미로찾기
# DFS를 사용한 미로찾기 풀이 -> 미로찾기는 BFS가 효율적인 듯

T = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def DFS(index):
    global result
    i = index[0]
    j = index[1]
    MAP[i][j] = '1'
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if (0 <= ni < N) and (0 <= nj < N) and MAP[ni][nj] == '0':
            DFS([ni, nj])
        if [ni, nj] == end:
            result = True
            return

for test in range(1, T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)] # 2차원 리스트로 읽어들임

    # 출발점, 도착점 찾기
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == '2':
                start = [row, col]
            if MAP[row][col] == '3':
                end = [row, col]

    result = False
    DFS(start)

    print(f'#{test} {int(result)}')

