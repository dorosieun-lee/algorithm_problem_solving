# SWEA 5188 최소합

T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    n = 1
    cap = 0
    while n <= (N-1)*(N-1):
        for i in range(cap, n - cap + 1):
            j = n - i
            if (i-1 >= 0) and (j-1 >= 0):
                MAP[i][j] += min(MAP[i-1][j], MAP[i][j-1])
            elif (i-1 < 0) and (j-1 >= 0):
                MAP[i][j] += MAP[i][j - 1]
            elif (i-1 >= 0) and (j-1 < 0):
                MAP[i][j] += MAP[i - 1][j]

        n += 1
        if n >= N:
            cap += 1

    print(f'#{test} {MAP[N-1][N-1]}')

'''
강사님 풀이
-> 완전탐색
def findMinvalue(x,y,value):
    # print(x,y,value)
    global result
    if x == N - 1 and y == N - 1: #도착점에 도착했을때
        result = min(result, value)
        return

    if 0 <= x + 1 < N:
        findMinvalue(x+1,y,value + MAP[x+1][y])

    if 0 <= y + 1 < N:
        findMinvalue(x,y+1,value + MAP[x][y+1])

T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    result = float("inf")
    findMinvalue(0,0,MAP[0][0])
    print(f'#{t} {result}')
'''