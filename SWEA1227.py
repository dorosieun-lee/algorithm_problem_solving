# SWEA 1227 미로2

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def BFS(start):
    global result
    queue = [start]

    while queue:
        n = queue.pop(0)
        for k in range(4):
            i = n[0] + di[k]
            j = n[1] + dj[k]
            if (0 <= i < N) and (0 <= j < N):
                if MAP[i][j] == 0: # 방문한 적 없는, 갈 수 있는 길이면
                    queue.append([i, j]) # 큐에 넣기
                    MAP[i][j] = 1 # 방문 표시
                if [i,j] == end:
                    result = 1
                    return


for _ in range(1, 11):
    N = 100
    test = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)] # 100x100 이차원 행렬

    # 시작점과 끝점 찾기
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                start = [row, col]
            if MAP[row][col] == 3:
                end = [row, col]

    result = 0
    BFS(start)

    print(f'#{test} {result}')
