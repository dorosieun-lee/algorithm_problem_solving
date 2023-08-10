# 재귀함수로 fibo
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# memoization 써서 fibo
def fibo(n):
    global memo
    if n > 1 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

# memo = [0] * n
# memo[0] = 0
# memo[1] = 1
# fibo(n)

# dp 개념으로 fibo

# DFS 구현
"""
입력방식
V E (vertex 개수, edge 개수)
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
-> VxV 행렬(인접행렬)로 표시해서 arr[v][w] = 1 이 edge(연결고리)가 있음을 의미하도록 저장할 수 있음
-> 인접 리스트 또는 딕셔너리로 저장할 수 있음
"""
def dfs_dict(n, V, adj_dict):
    visited = [0] * (V+1) # visited 만들어 -> index 0부터 V까지
    visited[n] = 1
    stack = [n] # stack 만들어 (시작점 넣어서)
    print(n, end = ' ')
    while True:
        # 인접한 w 있는지 찾고, 방문 안했으면 거기로 이동
        for w in adj_dict[n]:
            if visited[w] == 0:
                n = w # w로 이동 -> w가 n이 됨
                stack.append(n) # stack에 push
                visited[n] = 1 # n에 방문했음 마크 남기기
                print(n, end = ' ')
                break # for문 탈출

        else: # 인접한 w 가 없거나 모두 방문했을 경우
            if stack: # stack이 남아있으면
                n = stack.pop()
                #print('back', n, end = ' ')
            else: # stack 이 비어있으면
                break # while문 탈출

    print('\nnot visited vertex number:', V - visited.count(1))


V, E = list(map(int, input().split()))
edges = list(map(int, input().split()))

adj_dict = {i : [] for i in range(1, V+1)}
for key in adj_dict:
    for i in range(0, len(edges), 2):
        if key == edges[i]:
            adj_dict[key].append(edges[i+1])
        if key == edges[i+1]:
            adj_dict[key].append(edges[i])

dfs_dict(1, V, adj_dict)
# visited = [0] * (node의 개수)
# stack = []
# for key in vertex:
#     if visited[vertex-1] == True: # 되돌아가
#         pass
#     else: # 방문 안했어? -> 진행해
#         visited[vertex-1] = True # 방문했음 표시
#         stack.append(vertex)
#         pass

# 인접 행렬로 풀이
def dfs_arr(n, V, adj_m): # V: 마지막 정점 번호
    stack = [n]# stack 생성
    visited = [0] * (V+1) # visited 생성
    visited[n] = 1 # 시작점 방문 표시
    print(n, end=' ') # do[n]
    while True:
        for w in range(1, V+1): # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                # push(v)
                # do(w)
                n = w
                stack.append(n) # stack에 푸시
                visited[n] = 1 # 방문 표시
                print(n, end=' ')
                break
        else: # break를 못 만나고 for문을 다 돌았을 경우 (인접한 w가 없는 경우)
            if not stack: # stack이 비어있다면, break (-> while문에 대한 break)
                break
            else: # stack이 비어있지 않다면, 이전 정점으로 감
                n = stack.pop()


# V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 연결고리
# arr = list(map(int, input().split()))
# adj_m = [[0]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
#
# dfs_arr(1, V, adj_m)
#


