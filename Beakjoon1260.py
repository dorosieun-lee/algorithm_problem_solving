# Baekjoon1260 DFS와 BFS

def DFS(start):
    DFS_visited[start] = True
    for w in adj_list[start]:
        if not DFS_visited[w]:
            print(nodes[w], end=' ')
            DFS(w)

def BFS(start):
    queue = [start]
    BFS_visited[start] = True
    while queue:
        n = queue.pop(0)
        for w in adj_list[n]:
            if not BFS_visited[w]:
                queue.append(w)
                BFS_visited[w] = True
                print(nodes[w], end=' ')


N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
nodes = []
for edge in edges:
    nodes.extend(edge) # 간선이 존재하는, 즉 사용되는 정점의 번호

nodes = sorted(list(set(nodes)))
N_use = len(nodes) # 사용되는 정점의 개수

if V not in nodes: # 시작 정점 V와 연결된 간선이 존재하지 않는 경우
    print(V)
    print(V)

else:
    adj_list = [[] for _ in range(N_use)]
    for edge in edges:
        adj_list[nodes.index(edge[0])].append(nodes.index(edge[1]))
        adj_list[nodes.index(edge[1])].append(nodes.index(edge[0]))
    for lst in adj_list:
        lst.sort()

    DFS_visited = [False] * N_use
    BFS_visited = [False] * N_use
    print(V, end=' ')
    DFS(nodes.index(V))
    print(f'\n{V}', end=' ')
    BFS(nodes.index(V))
