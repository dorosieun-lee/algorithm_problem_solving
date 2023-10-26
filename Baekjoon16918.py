# Baekjoon 16918 봄버맨
R, C, N = map(int, input().split())

def put_bomb(MAP, bomb):
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == 0:  # 빈 칸에 폭탄 놓기
                MAP[row][col] = bomb


def explode_bomb(MAP, bomb):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    tmp = []
    counter_bomb = 1 if bomb == 2 else 2
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == counter_bomb:  # 폭탄 있는 칸 터뜨리기 -> 빈칸으로 만들기
                MAP[row][col] = 0
                tmp.append([row, col])

    for row, col in tmp: # 위에서 미리 주변 네 칸까지 터뜨리면서 폭탄칸이 주변 칸으로 터져버리면 그 폭탄으로 인한 주변 네 칸 터짐이 발생하지 않아서 따로 계산함
        for k in range(4):
            ni, nj = row + di[k], col + dj[k]
            if (0 <= ni < R) and (0 <= nj < C):
                MAP[ni][nj] = 0


init_MAP = [list(input()) for _ in range(R)]
MAP = [[0] * C for _ in range(R)]
for row in range(R):
    for col in range(C):
        if init_MAP[row][col] == 'O':
            MAP[row][col] = 1

if N % 2 == 0: # 짝수면 -> 폭탄 가득 판
    MAP = [['O'] * C for _ in range(R)]
    for line in MAP:
        print(''.join(line))

else:
    sec = 1
    bomb = 1  # 폭탄의 번호
    while sec < N:
        sec += 1
        if sec % 2 == 0:  # 짝수 초 => 폭탄 놓기
            bomb = 1 if bomb == 2 else 2  # 폭탄 번호 바꾸기
            put_bomb(MAP, bomb)
        else:  # 홀수 초 => 폭탄 터지기
            explode_bomb(MAP, bomb)

    # 숫자 맵을 다시 문자맵으로 변경
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == 0:
                MAP[row][col] = '.'
            else:
                MAP[row][col] = 'O'

    for line in MAP:
        print(''.join(line))