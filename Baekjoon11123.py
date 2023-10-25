# 백준 11123 양 한마리 양 두마리

from collections import deque


def BFS(row, col):
    global count, visited

    visited[row][col] = True
    queue = deque()
    queue.append([row, col])

    while queue:
        now = queue.popleft()

        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:  # 상하좌우 돌면서
            ni, nj = now[0] + di, now[1] + dj
            # ni, nj가 MAP의 범위 안이고, 방문한 적이 없는 곳이며, 양에 해당할 때
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and MAP[ni][nj] == '#':
                visited[ni][nj] = True  # 방문 처리
                queue.append([ni, nj])  # queue에 추가

    count += 1  # 양 무리 + 1
    return


T = int(input())

for test in range(1, T + 1):
    H, W = map(int, input().split())
    MAP = [input() for _ in range(H)]

    count = 0
    visited = [[False] * W for _ in range(H)]
    for row in range(H):
        for col in range(W):
            # 양에 해당하면서, 방문한 적이 없는 곳인 경우
            if MAP[row][col] == '#' and not visited[row][col]:
                BFS(row, col)
            # 양이 아니더라도 방문 표시 남기기 -> 굳이 없어도 될 듯
            visited[row][col] = True

    print(count)
