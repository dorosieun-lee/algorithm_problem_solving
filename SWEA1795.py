# SWEA 1795 인수의 생일 파티

import heapq
def dijkstra(start, direction):
    heap = []
    heapq.heappush(heap, [0, start])
    times[start] = 0
    if direction == "fromX":
        adj = adj_arr
    else:
        adj = adj_arr_re

    while heap:
        time, now = heapq.heappop(heap)

        if time > times[now]:
            continue

        for next in range(1, N+1):
            if adj[now][next] != 0: # now 와 next가 연결되어 있는 경우
                new_time = time + adj[now][next] # 걸리는 시간을 더하고
                if new_time < times[next]: # times에 이미 저장된 것보다 작다면
                    times[next] = new_time # times에 저장(최소를 저장)
                    heapq.heappush(heap, (new_time, next)) # heap에 저장 -> 다음으로 갈 번호로 저장


T = int(input())
for test in range(1, T+1):
    N, M, X = map(int, input().split())
    adj_arr = [[0]*(N+1) for _ in range(N+1)]
    adj_arr_re = [[0]*(N+1) for _ in range(N+1)] # 방향 반대로
    for _ in range(M):
        f, t, w = map(int, input().split())
        adj_arr[f][t] = w
        adj_arr_re[t][f] = w

    min_time = [0] * (N+1)
    # X 에서 각 집으로 돌아가는 최단 시간
    times = [float("inf")] * (N + 1)
    dijkstra(X, "fromX")
    # print('X에서 각 집으로 돌아가는 최단 시간: ', times)
    for i in range(1, N+1):
        min_time[i] += times[i]

    # 각 집에서 X로 가는 최단 시간
    times = [float("inf")] * (N + 1)
    dijkstra(X, "toX")
    # print('각 집에서 X로 가는 최단 시간: ', times)
    for i in range(1, N+1):
        min_time[i] += times[i]

    print(f'#{test} {max(min_time)}')
