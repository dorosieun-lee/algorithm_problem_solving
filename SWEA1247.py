# SWEA 1247 최적경로

def perm(n, front, dist):
    global MIN
    if dist > MIN:
        return
    if n == N:
        dist += abs(lst[-1][0] - lst[front][0]) + abs(lst[-1][1] - lst[front][1]) # 마지막 고객 집에서 집 사이의 거리
        MIN = min(dist, MIN)
        return

    for i in range(1, N+1):
        if used[i] == 0:
            used[i] = 1
            add = abs(lst[front][0] - lst[i][0]) + abs(lst[front][1] - lst[i][1])
            perm(n+1, i, dist+add)
            used[i] = 0


T = int(input())
for test in range(1, T+1):
    N = int(input())
    points = list(map(int, input().split()))
    start = (points[0], points[1])
    end = (points[2], points[3])
    lst = [start]
    for i in range(4, len(points), 2):
        lst.append((points[i], points[i+1]))
    lst.append(end)

    index = list(range(1, N+1)) # 1, 2, 3, ..., N
    used = [0] * (N+1)
    MIN = float("inf")
    perm(0, 0, 0)

    print(f'#{test} {MIN}')