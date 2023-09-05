# baekjoon 2606 바이러스

# 연결된 컴퓨터는 바이러스에 걸린다
# 감염된 컴퓨터 수?
# 시작은 1번 컴퓨터

from collections import deque

def BFS(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        n = queue.popleft()
        for w in adj_list[n]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
                cnt += 1

N = int(input()) # 컴퓨터 수
N_edge = int(input()) # 연결된 컴퓨터 쌍의 수
edges = [list(map(int, input().split())) for _ in range(N_edge)]

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for edge in edges: # 방향이 없는 그래프!!!!!!!
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

cnt = 0
BFS(1)

print(cnt)
