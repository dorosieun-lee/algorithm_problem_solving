# 백준 2211 네트워크 복구
# 슈퍼컴퓨터(1번)에서부터 모든 컴퓨터까지 최단 시간이 걸리는 회선의 개수 및 회선 구하기 -> 다익스트라
import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        weight, now = heapq.heappop(heap)

        if dist[now] < weight:
            continue

        for next, cost in graph[now]:
            new_cost = weight + cost
            if dist[next] <= new_cost:
                continue
            else:
                dist[next] = new_cost
                path[next] = now
                heapq.heappush(heap, (new_cost, next))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t, w = map(int, input().split())
    # 양방향 그래프
    graph[f].append([t, w])
    graph[t].append([f, w])

dist = [float("inf")] * (N + 1)
path = [0] * (N+1)
dijkstra(1)

print(N-1)
for i, p in enumerate(path[2:]):
    print(i+2, p)