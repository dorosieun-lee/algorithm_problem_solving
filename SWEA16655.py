# SWEA 16655 노드의 거리

def BFS(S, V):
    while queue:
        n = queue.pop(0)
        for w in adj_list[n]:
            if visited[w] == 0: # 방문한 적 없는 노드면
                visited[w] = visited[n] + 1
                queue.append(w)

T = int(input())

for test in range(1, T+1):
    V, E = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    for edge in edges: # 방향이 정해져 있지 않으므로, 양쪽 다 추가해줘야함
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [0] * (V+1)
    visited[S] = 1
    queue = [S]ㄴ

    BFS(S, V)
    print(f'#{test} {max(0, visited[G]-1)}') # 연결되어 있지 않는 경우, -1을 반환할테니 -> max(0, result) 를 통해서 -1이 되면 0을 반환하도록 설정

