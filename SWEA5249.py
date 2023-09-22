# SWEA 5249 최소 신장 트리

import heapq
def PRIM(start):
    global sum_weight
    heap = []
    heapq.heappush(heap, [0, start])
    visited = [False] * (V+1)

    while heap:
        #print(heap)
        weight, now = heapq.heappop(heap)
        if all(visited):
            break
        if visited[now]:
            continue

        sum_weight += weight
        visited[now] = True
        for next, cost in adj_list[now]:
            if not visited[next]:
                heapq.heappush(heap, [cost, next])


T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for i in range(V+1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        # 양방향
        adj_list[f].append([t, w])
        adj_list[t].append([f, w])

    sum_weight = 0
    PRIM(0)
    print(f'#{test} {sum_weight}')