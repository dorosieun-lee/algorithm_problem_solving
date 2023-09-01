# SWEA 1953 탈주범 검거

# 탈주범이 있을 수 있는 위치의 개수를 계산

# 탈주범은 시간당 1의 거리를 움직일 수 있다
# 지하 터널
# 1: 상하좌우에 있는 터널과 연결
# 2: 상하에 있는 터널이 연결
# 3: 좌우에 있는 터널이 연결
# 4: 상우에 있는 터널이 연결
# 5: 하우에 있는 터널이 연결
# 6: 하좌에 있는 터널이 연결
# 7: 상좌에 있는 터널이 연결

# 각 방향에 일치하는 row, col 델타
move = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}

# 파이프 번호 별 움직일 수 있는 방향
pipe = {1: ['up', 'down', 'right', 'left'],
        2: ['up', 'down'],
        3: ['right', 'left'],
        4: ['up', 'right'],
        5: ['down', 'right'],
        6: ['down', 'left'],
        7: ['up', 'left']}

# 현재 파이프와 연결될 수 있는 파이프의 번호
next_pipe = {'up': [1, 2, 5, 6],
             'down': [1, 2, 4, 7],
             'right': [1, 3, 6, 7],
             'left': [1, 3, 4, 5]}

from collections import deque
def check_and_move(row, col, L): # BFS 방식
    queue = deque()
    queue.append((row, col))
    visited = [[0] * M for _ in range(N)]
    visited[row][col] = 1

    while queue:
        nr, nc = queue.popleft()
        direction = pipe[MAP[nr][nc]]

        for d in direction:
            ni = nr + move[d][0]
            nj = nc + move[d][1]
            if (0 <= ni < N) and (0 <= nj < M) and visited[ni][nj] == 0:  # 경계 안에 있고, 방문한 적 없는 곳이면
                if MAP[ni][nj] in next_pipe[d]:  # 그 방향에 이동할 수 있는 파이프가 있으면
                    visited[ni][nj] = visited[nr][nc] + 1 # 최단거리 표시이자 방문 표시
                    queue.append((ni, nj))

    return visited

def count_move(visited):
    cnt = 0
    for row in range(N):
        for col in range(M):
            if 0 < visited[row][col] <= L:
                cnt += 1

    return cnt


T = int(input())
for test in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # 세로, 가로, 멘홀 세로 위치, 멘홀 가로 위치, 탈출 후 소요된 시간
    MAP = [list(map(int, input().split())) for _ in range(N)] # NxM

    visited = check_and_move(R, C, L)

    # for line in visited:
    #     print(line)

    result = count_move(visited)

    print(f'#{test} {result}')