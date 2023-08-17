# Baekjoon 18352 특정 거리의 도시 찾기
# DFS, BFS 둘다 써야하는 것 같은데..!
# X에서 출발해서 다른 노드로 가는 최단거리가 K인 노드를 출력
# 미완성...
# https://www.acmicpc.net/problem/18352

def find_path(start, route, K):
    if len(route) <= K:
        path.append(route)
        if len(route) == K:
            return
    for n in range(1, N+1):
        #print(start, n)
        if adj_arr[start][n] == 1: # 길이 있다
            #print(route)
            find_path(n, route + [n], K)

N, M, K, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
flag = False

adj_arr = [[0]* (N+1) for _ in range(N+1)] # NxN 0으로 가득찬 행렬
for edge in edges:
    adj_arr[edge[0]][edge[1]] = 1 # edge[0]에서 edge[1] 로 가는 길이 존재함을 표시

path = []
find_path(X, [], K)
# X 지점에서 K번 이내로 움직여서 갈 수 있는 경로 다 찾았음
path.remove([])
my_dict = {i: [] for i in range(1, N+1)}
for p in path:
    my_dict[p[-1]].append(len(p))

for k, v in my_dict.items():
    if v and min(v) == K:
        flag = True
        print(k)


if not flag:
    print(-1)

print(path)