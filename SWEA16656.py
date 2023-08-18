# SWEA 16656 미로의 거리
# -> BFS는 재귀함수를 쓰지 않고 queue로만 작성하는게 일반적이다.(ChatGPT 왈)

def BFS():
    while queue:
        start = queue.pop(0)
        for k in range(4):
            i = start[0] + di[k]
            j = start[1] + dj[k]
            if (0 <= i < N) and (0 <= j < N): # 경계 안쪽
                if MAP[i][j] == 'end':  # 3 만났다! -> 거기까지 가는데 필요한 거리 반환
                    return MAP[start[0]][start[1]] - 1
                elif MAP[i][j] == 0: # 갈 수 있는 길이면
                    queue.append([i, j]) # queue에 추가
                    MAP[i][j] = MAP[start[0]][start[1]] + 1 # 지금까지 온 거리 추가
    return 0

T = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)]

    # 시작점, 도착점 찾기
    for row in range(N):
        if 2 in MAP[row]:
            col = MAP[row].index(2)
            start = [row, col]
        elif 3 in MAP[row]:
            col = MAP[row].index(3)
            end = [row, col]

    MAP[end[0]][end[1]] = 'end'
    queue = [start]
    MAP[start[0]][start[1]] = 1 # 시작지점도 거리 +1
    result = BFS()
    # print(MAP)

    print(f'#{test} {result}')