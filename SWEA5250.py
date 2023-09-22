# SWEA 5250 최소 비용
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
import heapq
def dijkstra(start):
    global cnt
    heap = []
    heapq.heappush(heap, [0, start, 1])
    minimum[start[0]][start[1]] = 0

    while heap:
        dist, now, direction = heapq.heappop(heap)
        if minimum[now[0]][now[1]] < dist:
            continue
        cnt += 1
        for k in range(4):
            ni, nj = now[0] + di[k], now[1] + dj[k]
            if (0 <= ni < N) and (0 <= nj < N):
                new_dist = dist + 1
                if MAP[now[0]][now[1]] < MAP[ni][nj]:
                    new_dist += MAP[ni][nj] - MAP[now[0]][now[1]]
                if minimum[ni][nj] > new_dist:
                    heapq.heappush(heap, [new_dist, [ni, nj], k])
                    minimum[ni][nj] = new_dist


T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    minimum = [[float("inf")] * N for _ in range(N)]
    cnt = 0
    dijkstra([0, 0])
    # print(minimum)
    result = minimum[-1][-1]
    print(cnt)
    print(f'#{test} {result}')