# 프로그래머스 리코쳇 로봇
def find_robot(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'R':
                return (row, col)


def go_robot(row, col, cnt):
    if board[row][col] == 'G':
        return
    #
    for k in range(4):
        while True:
            ni, nj = i + di[key], j + dj[key]
            # 벽을 만나거나 장애물을 만나면 회전
            if board[ni][nj] == 'D' or ni == 0 or ni == len(board) or nj == 0 or nj == len(board[0]):
                go_robot(ni, nj, cnt + 1)


def solution(board):
    # 방향: 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    key = 0  # 초기 설정
    i, j = find_robot(board)
    while True:
        ni, nj = i + di[key], j + dj[key]
        if board[ni][nj] == 'D':

    answer = 0
    return answer

