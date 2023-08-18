# SWEA 1226 미로1

def BFS(start):
    di = [1, 0 ,-1, 0]
    dj = [0, 1, 0, -1]
    queue.append(start)
    MAP[start[0]][start[1]] = 1 # queue에 넣었던 곳 -> 방문한 곳 -> 벽이나 마찬가지
    while queue:
        start = queue.pop(0)
        for k in range(4):
            i = start[0] + di[k]
            j = start[1] + dj[k]
            if (0 <= i < 16) and (0 <= j < 16):
                if MAP[i][j] == 3:
                    return True
                if MAP[i][j] != 1:
                    queue.append([i, j])
                    MAP[i][j] = 1 # queue에 넣었던 곳 -> 방문한 곳 -> 벽이나 마찬가지
    return False



for _ in range(1, 11):
    test = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(16)] # 16x16 0,1,2,3으로 이루어진 행렬

    for row in range(16):
        try:
            col = MAP[row].index(2)
            break
        except:
            continue

    start = [row, col]
    queue = []
    result = BFS(start)
    print(f'#{test} {int(result)}')