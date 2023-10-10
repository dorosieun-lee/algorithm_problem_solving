# 프로그래머스 프렌즈4블록
# 블록 제거 후 떨어지는거 구현 주의!

def is_2x2(start, board):
    if board[start[0]][start[1]].isalpha(): # 2x2 블럭이 모두 ''인 경우 방지
        if board[start[0]][start[1]] == board[start[0]][start[1]+1] and board[start[0]][start[1]] == board[start[0]+1][start[1]] and board[start[0]+1][start[1]] == board[start[0]+1][start[1]+1]:
            return True
    return False

def remove(points, board, score):
    di = [0, 0, 1, 1]
    dj = [0, 1, 0, 1]
    for p in points:
        for k in range(4):
            if board[p[0] + di[k]][p[1] + dj[k]] != '':
                score += 1
            board[p[0] + di[k]][p[1] + dj[k]] = ''
    # print('remove', board)
    return board, score

def move(m, n, board):
    for row in range(m-1, 0, -1):
        for col in range(n):
            if board[row][col] == '':
                tmp_row = row
                while True:
                    tmp_row -= 1
                    if tmp_row == -1:
                        break
                    if board[tmp_row][col].isalpha():
                        board[row][col], board[tmp_row][col] = board[tmp_row][col], board[row][col] # swap
                        break
    # print('move', board)
    return board

def solution(m, n, board):
    board = [list(line) for line in board]
    score = 0
    while True:
        # 초기화
        points = []
        flag = True
        for row in range(m-1):
            for col in range(n-1):
                if is_2x2([row, col], board):
                    points.append((row, col)) # 2x2 같은 타일인 지점의 좌측 상단 지점번호 담기
                    flag = False
        board, score = remove(points, board, score)
        board = move(m, n, board)
        if flag: # 보드를 다 돌았지만, is_2x2에 걸리는게 하나도 없는 경우 -> while문 종료
            break

    return score


board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# board = ['AAAAAA', 'AAAAAA', 'AAAAAA', 'AAAAAA', 'AAAAAA', 'AAAAAA']
# board = ['ABCDEF', 'ABCDEF', 'ABCDEF', 'ABCDEF', 'ABCDEF', 'ABCDEF']
print(solution(6, 6, board))