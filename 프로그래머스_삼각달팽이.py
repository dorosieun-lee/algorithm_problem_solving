# 프로그래머스 삼각 달팽이

def solution(n):
    # 삼각형에 해당하는 배열을 만들자.
    tri = [[0]*i for i in range(1, n+1)]

    di = [1, 0, -1]
    dj = [0, 1, -1]

    num = 0
    dir = 0 # 0: 아래, 1: 오른쪽, 2: 왼쪽 상단으로 대각선 방향
    wall = n # 한 방향으로 갈 수 있는 길이
    path = 0 # 한 방향으로 지나온 길이
    i, j = -1, 0
    while True:
        i += di[dir]
        j += dj[dir]
        num += 1
        path += 1
        tri[i][j] = num
        if path == wall:
            dir = (dir+1)%3
            wall -= 1
            path = 0
            if wall == 0:
                break
    answer = []
    for line in tri:
        answer.extend(line)
    return answer

n = 4
print(solution(n))
n = 5
print(solution(n))
n = 6
print(solution(n))