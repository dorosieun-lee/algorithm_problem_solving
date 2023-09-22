# 프로그래머스 방문 길이

def solution(dirs):
    horizontal = [[False] * 10 for _ in range(11)]
    vertical = [[False] * 11 for _ in range(10)]

    position = [0, 0]
    for dir in dirs:
        #print(position)
        if dir == 'U':
            x = position[1] + 5
            y = position[0] + 5
            #print('path: ', x, y)
            if (0 <= x < len(vertical)) and (0 <= y < len(vertical[0])):
                vertical[x][y] = True
                position[0], position[1] = position[0], position[1]+1
        elif dir == 'D':
            x = position[1] + 4
            y = position[0] + 5
            #print('path: ', x, y)
            if (0 <= x < len(vertical)) and (0 <= y < len(vertical[0])):
                vertical[x][y] = True
                position[0], position[1] = position[0], position[1]-1
        elif dir == 'R':
            x = position[1] + 5
            y = position[0] + 5
            #print('path: ', x, y)
            if (0 <= x < len(horizontal)) and (0 <= y < len(horizontal[0])):
                horizontal[x][y] = True
                position[0], position[1] = position[0]+1, position[1]
        elif dir == 'L':
            x = position[1] + 5
            y = position[0] + 4
            #print('path: ', x, y)
            if (0 <= x < len(horizontal)) and (0 <= y < len(horizontal[0])):
                horizontal[x][y] = True
                position[0], position[1] = position[0]-1, position[1]

    total = 0
    for line in horizontal:
        total += sum(line)
    for line in vertical:
        total += sum(line)

    return total


dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
print(solution(dirs))

"""
다른 사람 풀이
신박하고 진관적이야...!

def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
"""