# SWEA 1861 정사각형 방
import sys
sys.setrecursionlimit(100000)
# 기본 설정이 재귀함수 실행 횟수가 1000번 이상이면 recursion error 뜨게 되어 있으므로 해당 문제에서는 확장해줘야함

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def DFS(row, col, go, start):
    global MAX, case
    #print(go)
    num = room[row][col]
    for k in range(4):
        i, j = row + di[k], col + dj[k]
        if (0 <= i < N) and (0 <= j < N) and room[i][j] == num+1:
            #print('check: ', room[i][j])
            DFS(i, j, go+1, start)

    if go > MAX:
        MAX = go
        case = [start]
    elif go == MAX:
        case += [start]
    elif go < MAX:
        return


T = int(input())
for test in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0
    case = []
    for row in range(N):
        for col in range(N):
            DFS(row, col, 0, room[row][col])

    result = (min(case), MAX+1)
    print(f'#{test}', *result)