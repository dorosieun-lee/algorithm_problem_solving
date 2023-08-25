# SWEA 1873 상호의 배틀필드

def shoot(row, col):
    global stop
    if MAP[row][col] == '*': # 벽돌로 만들어진 벽이면
        MAP[row][col] = '.' # 평지로 바뀜
        stop = True # 멈춤
    elif MAP[row][col] == '#': # 강철로 만들어진 벽이면
        stop = True # 아무일도 일어나지 않고 멈춤


T = int(input())

for test in range(1, T+1):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    input()
    move = input()

    # 시작 지점 찾기
    for row in range(H):
        line = MAP[row]
        if '>' in line:
            col = line.index('>')
            point = [row, col]
            break
        elif '<' in line:
            col = line.index('<')
            point = [row, col]
            break
        elif '^' in line:
            col = line.index('^')
            point = [row, col]
            break
        elif 'v' in line:
            col = line.index('v')
            point = [row, col]
            break

    for m in move:
        if m == 'U':
            MAP[point[0]][point[1]] = '^' # 전차가 바라보는 방향을 위쪽으로 바꾸고
            if (0 <= point[0]-1 < H): # MAP 밖으로 벗어나지 않고
                if MAP[point[0]-1][point[1]] == '.': # 위쪽이 평지라면
                    MAP[point[0]][point[1]], MAP[point[0]-1][point[1]] = MAP[point[0]-1][point[1]], MAP[point[0]][point[1]] # 자리바꾸기
                    point[0] -= 1
        elif m == 'D':
            MAP[point[0]][point[1]] = 'v' # 전차가 바라보는 방향을 아래쪽으로 바꾸고
            if (0 <= point[0]+1 < H): # MAP 밖으로 벗어나지 않고
                if MAP[point[0]+1][point[1]] == '.': # 아래쪽이 평지라면
                    MAP[point[0]][point[1]], MAP[point[0]+1][point[1]] = MAP[point[0]+1][point[1]], MAP[point[0]][point[1]] # 자리바꾸기
                    point[0] += 1
        elif m == 'L':
            MAP[point[0]][point[1]] = '<' # 전차가 바라보는 방향을 왼쪽으로 바꾸고
            if (0 <= point[1]-1 < W): # MAP 밖으로 벗어나지 않고
                if MAP[point[0]][point[1]-1] == '.': # 왼쪽이 평지라면
                    MAP[point[0]][point[1]], MAP[point[0]][point[1]-1] = MAP[point[0]][point[1]-1], MAP[point[0]][point[1]] # 자리바꾸기
                    point[1] -= 1
        elif m == 'R':
            MAP[point[0]][point[1]] = '>' # 전차가 바라보는 방향을 오른쪽으로 바꾸고
            if (0 <= point[1]+1 < W): # MAP 밖으로 벗어나지 않고
                if MAP[point[0]][point[1]+1] == '.': # 오른쪽이 평지라면
                    MAP[point[0]][point[1]], MAP[point[0]][point[1]+1] = MAP[point[0]][point[1]+1], MAP[point[0]][point[1]] # 자리바꾸기
                    point[1] += 1
        elif m == 'S': # 포탄 발사!!!
            if MAP[point[0]][point[1]] == '>':
                row = point[0]
                stop = False
                for col in range(point[1]+1, W):
                    shoot(row, col)
                    if stop:
                        break
            elif MAP[point[0]][point[1]] == '<':
                row = point[0]
                stop = False
                for col in range(point[1]-1, -1, -1):
                    shoot(row, col)
                    if stop:
                        break
            elif MAP[point[0]][point[1]] == '^':
                col = point[1]
                stop = False
                for row in range(point[0]-1, -1, -1):
                    shoot(row, col)
                    if stop:
                        break
            elif MAP[point[0]][point[1]] == 'v':
                col = point[1]
                stop = False
                for row in range(point[0]+1, H):
                    shoot(row, col)
                    if stop:
                        break

    print(f'#{test}', end=' ')
    for line in MAP:
        print(''.join(line))