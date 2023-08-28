# Baekjoon 10158 개미

def change_direction(key, p, q):
    if [p, q] in [[0,0], [w, 0], [0, h], [w, h]]: # 네 꼭짓점에 도달한 경우
        if key == 0: key = 2
        elif key == 1: key = 3
        elif key == 2: key = 0
        elif key == 3: key = 1
    elif (p == w) and (0 < q < h): # 오른쪽 벽
        if key == 0: key = 1
        elif key == 3: key = 2
    elif (0 < p < w) and (q == h): # 위쪽 벽
        if key == 0: key = 3
        elif key == 1: key = 2
    elif (p == 0) and (0 < q < h): # 왼쪽 벽
        if key == 1: key = 0
        elif key == 2: key = 3
    elif (0 < p < w) and (q == 0): # 아래쪽 벽
        if key == 2: key = 1
        elif key == 3: key = 0
    return key

import sys
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

move = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
key = 0

while t > 0:
    if key == 0:
        dt = min(w-p, h-q)
    elif key == 1:
        dt = min(p, h-q)
    elif key == 2:
        dt = min(p, q)
    elif key == 3:
        dt = min(w-p, q)

    if t >= dt:
        p = p + move[key][0] * dt
        q = q + move[key][1] * dt
        t -= dt
    else:
        p = p + move[key][0] * t
        q = q + move[key][1] * t
        t = 0
    if (p == 0) or (p == w) or (q == 0) or (q == h):
        key = change_direction(key, p, q)

print(p, q)
