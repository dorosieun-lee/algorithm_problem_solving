# 4614 재미있는 오셀로 게임

# 우하좌상, 대각선 우상 우하 좌하 좌상
di = [0, 1, 0, -1, -1, 1, 1, -1]
dj = [1, 0, -1, 0, 1, 1, -1, -1]


def reverse(row, col, color):
    counter = 2 if color == 1 else 1
    for k in range(8):
        max_length = 0
        if (0 <= row+di[k] < N) and (0 <= col+dj[k] < N) and MAP[row+di[k]][col+dj[k]] == counter: # 한칸 멀리 있는게 상대편 돌이면,
            for l in range(2, N): # 두칸 뒤부터 살펴볼거야
                my_i = row + di[k] * l
                my_j = col + dj[k] * l
                if (0 <= my_i < N) and (0 <= my_j < N): # 경계 안에 있으면서
                    if MAP[my_i][my_j] == color: # 놓은 돌과 같은 색이면
                        max_length = l
                        break
                    elif MAP[my_i][my_j] == 0:
                        break
                    # counter면 한칸 더 살펴봄(l++)

        if max_length != 0:
            # 색 바꾸기
            for l in range(1, max_length):
                op_i = row + di[k] * l
                op_j = col + dj[k] * l
                MAP[op_i][op_j] = color


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [[0]*N for _ in range(N)] # NxN 바둑판
    MAP[N//2-1][N//2-1:N//2+1] = [2, 1]
    MAP[N//2][N//2-1:N//2+1] = [1, 2]

    for _ in range(M):
        row, col, color = map(int, input().split())
        MAP[row-1][col-1] = color
        reverse(row-1, col-1, color)
        # for line in MAP:
        #     print(line)
        # print()

    one_cnt, two_cnt = 0, 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                one_cnt += 1
            elif MAP[i][j] == 2:
                two_cnt += 1

    print(f'#{test} {one_cnt} {two_cnt}')