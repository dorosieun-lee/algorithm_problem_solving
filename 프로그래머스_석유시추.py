# 프로그래머스 석유 시추

from collections import deque


def solution(land):
    fuel_col = [0] * len(land[0])
    def find_fuel(r, c):
        queue = deque()
        queue.append([r, c])
        land[r][c] = 0
        cnt = 1
        col_set = set()
        while queue:
            x, y = queue.popleft()
            col_set.add(y)
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < row) and (0 <= ny < col) and land[nx][ny] == 1:
                    cnt += 1
                    land[nx][ny] = 0
                    queue.append([nx, ny])

        for c in list(col_set):
            fuel_col[c] += cnt

    row = len(land)
    col = len(land[0])

    for r in range(row):
        for c in range(col):
            if land[r][c] == 1:
                find_fuel(r, c)

    answer = max(fuel_col)
    return answer

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

print(solution(land))