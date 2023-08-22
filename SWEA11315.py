# SWEA 11315 오목 판정

T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    # for line in MAP:
    #     print(line)
    # print()

    flag = False
    direction = [(0,1), (1,0), (1,1), (1, -1)] # 오른쪽, 아래, 좌하 대각선, 우하 대각선

    for i in range(N):
        if flag:
            break
        for j in range(N):
            if MAP[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    ni, nj = i, j
                    while True:
                        ni += direction[k][0]
                        nj += direction[k][1]
                        if (0 <= ni < N) and (0 <= nj < N) and MAP[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break

                    if cnt >= 5:
                        flag = True

    result = 'YES' if flag else 'NO'
    print(f'#{test} {result}')