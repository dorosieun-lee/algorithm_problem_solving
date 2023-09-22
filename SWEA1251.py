# SWEA 1251 하나로
import math

def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x > y:
        parents[x] = y
    else:
        parents[y] = x

# KRUSKAL 알고리즘으로 풀이
T = int(input())
for test in range(1, T+1):
    N = int(input())
    x_points = list(map(int, input().split()))
    y_points = list(map(int, input().split()))
    E = float(input())

    parents = [i for i in range(N)]
    dist = []
    for i in range(N):
        for j in range(i+1, N):
            tmp = math.sqrt((x_points[i] - x_points[j])**2 + (y_points[i] - y_points[j])**2)
            dist.append([tmp, i, j]) # 거리, 출발 섬, 도착 섬

    dist.sort(key=lambda x: x[0])
    #print(dist)
    cost = 0
    cnt = 0
    for d, x, y in dist:
        cnt += 1
        if cnt >= N//2:
            SET = set()
            for i in range(N):
                SET.add(find_set(i))
            if len(SET) == 1:
                break

        if find_set(x) == find_set(y):
            continue
        cost += E * (d**2)
        union(x, y)
    result = int(round(cost, 0))
    print(f'#{test} {result}')

