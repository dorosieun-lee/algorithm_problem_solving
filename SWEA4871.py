# SWEA 4871 그래프 경로

def dfs(S, G, V, adj_dict):
    stack = [S]
    visited = [0] * (V+1)
    visited[S] = 1
    n = S
    while True:
        if n == G: # 지금 있는 노드가 가야하는 노드(G)이면, 끝내
            return 1

        for w in adj_dict[n]: # n번 노드와 연결된 노드들 중에서
            if visited[w] == 0: # 방문한 적 없는 노드면
                n = w # 거기로 가고
                stack.append(n) # stack에 추가하고
                visited[n] = 1 # 방문했음으로 표시
                break
        else: # 인접한 것들 중에 방문 안했던 노드 없으면
            if stack: # stack이 있는지 확인하고 -> 돌아갈 수 있는 곳이 있는지
                n = stack.pop() # 있으면, 돌아가
            else:
                break # 없으면, 끝내

    if visited[G] == 1:
        return 1
    else:
        return 0


T = int(input())

for test in range(1, T+1):
    V, E = list(map(int, input().split())) # 노드 개수, 간선 개수
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split())) # 출발노드, 도착노드

    adj_dict = {i: [] for i in range(1, V+1)}
    for key in adj_dict:
        for edge in edges:
            if key == edge[0]: # 방향성 있음!!!
                adj_dict[key].append(edge[1])

    print(f'#{test} {dfs(S, G, V, adj_dict)}')

