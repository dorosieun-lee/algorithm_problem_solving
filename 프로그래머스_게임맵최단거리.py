# 프로그래머스 게임 맵 최단거리

def BFS(start, visited, maps):
    visited[start[0]][start[1]] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    queue = [start]
    while queue:
        n = queue.pop(0)
        if n == [len(maps)-1, len(maps[0])-1]:
            return visited[n[0]][n[1]]

        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if (0 <= ni < len(visited)) and (0 <= nj < len(visited[0])) and visited[ni][nj] == 0 and maps[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = visited[n[0]][n[1]] + 1
    return -1


def solution(maps):
    if len(maps) == 1:
        if maps[0][-2] != 0:
            return len(maps[0])
        else:
            return -1
    if len(maps[0]) == 1:
        if maps[-2][0] != 0:
            return len(maps)
        else:
            return -1
    if maps[-1][-2] == 0 and maps[-2][-1] == 0:
        return -1

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = BFS([0, 0], visited, maps)
    return answer

maps = [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,1]]

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# maps = [[1,1],[1,1]]
print(solution(maps))