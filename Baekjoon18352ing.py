# Baekjoon 18352 특정 거리의 도시 찾기
# DFS, BFS 둘다 써야하는 것 같은데..!
# X에서 출발해서 다른 노드로 가는 최단거리가 K인 노드를 출력
# 미완성...
# https://www.acmicpc.net/problem/18352

def dfs_find_dist(N, X, adj_dict):
    visited = [0] * (N+1)
    n = X
    visited[n] = 1
    stack = []
    dist = {i: [] for i in range(1, N+1)}

    while True:
        for w in adj_dict[n]:
            if visited[w] == 0:
                n = w
                stack.append(n)
                visited[n] = 1
                if len(stack) == K:
                    print(stack)
                    Kpath_node.append(stack[-1])
                break

        else:
            if stack:
                n = stack.pop()
            else:
                return Kpath_node

# N: 도시의 개수, M: 도로의 개수, K: 찾고자하는 최단 거리, X: 출발지점
N, M, K, X = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

adj_dict = {i: [] for i in range(1, N+1)}
for edge in edges:
    adj_dict[edge[0]].append(edge[1])

Kpath_node = dfs_find_Kpath(N, X, K, adj_dict)
print(Kpath_node)