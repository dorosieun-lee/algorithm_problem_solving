# 프로그래머스 무인도 여행

# X는 바다
# 1-9 무인도, 식량 -> 식량을 다 합하면, 무인도에 몇일 머무를 수 있는지를 의미함

# 각 섬에서 몇일 머무를 수 있는지를 오름차순으로 담아 return
# 지낼 수 있는 무인도가 없다면 -1

def solution(MAP):
    MAP = [list(MAP[i]) for i in range(len(MAP))]
    # for line in MAP:
    #     print(line)
    nr = len(MAP) # 행 길이
    nc = len(MAP[0]) # 열 길이

    answer = []
    for i in range(nr):
        for j in range(nc):
            if MAP[i][j] != 'X':
                total = BFS(i, j, MAP, nr, nc)
                answer.append(total)

    return sorted(answer) if len(answer) != 0 else [-1]


def BFS(i, j, MAP, nr, nc):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    queue = [[i, j]]
    total = int(MAP[i][j])
    MAP[i][j] = 'X'
    while queue:
        a, b = queue.pop(0)
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if (0 <= ni < nr) and (0 <= nj < nc) and MAP[ni][nj] != 'X':
                queue.append([ni, nj])
                total += int(MAP[ni][nj])
                MAP[ni][nj] = 'X'  # 탐색했으니까 갈 수 없는 곳으로 만들어버림
    return total

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))
