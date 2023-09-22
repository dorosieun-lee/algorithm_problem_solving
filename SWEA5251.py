# SWEA 5251 최소 이동 거리

import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        weight, now = heapq.heappop(heap)

        # 이미 방문한 지점이면서, 누적거리보다 더 짧게 방문한 적이 있다면 pass
        if dist[now] < weight:
            continue

        for next, cost in graph[now]:
            new_cost = weight + cost
            # 누적거리가 기존보다 크거나 같다
            if dist[next] <= new_cost:
                continue
            else:
                dist[next] = new_cost
                heapq.heappush(heap, (new_cost, next))


T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 리스트로 구현
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f].append([t, w]) # 단방향 그래프

    # 누적 거리를 계속 저장
    dist = [float("inf")] * (V+1)  # 더 작은 걸 저장해야하니까 기본으로 엄청 큰 수를 저장함
    dijkstra(0)
    print(f'#{test} {dist[-1]}')