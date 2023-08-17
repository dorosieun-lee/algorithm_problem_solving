# Baekjoon 18352 특정 거리의 도시 찾기
# DFS, BFS 둘다 써야하는 것 같은데..!
# X에서 출발해서 다른 노드로 가는 최단거리가 K인 노드를 출력
# https://www.acmicpc.net/problem/18352

# 테스트 케이스로 제시된 것은 됨
# 채점 결과 fail~~~, 시간초과 뜸...ㅎㅎ

def find_path(start, route, K):
    # K 이상은 가지 않겠다.
    if len(route) <= K:
        path.append(route)
        # 기저조건: 거리가 K인 경우
        if len(route) == K:
            return
    for n in range(1, N+1):
        #print(start, n)
        if adj_arr[start][n] == 1: # 길이 있다
            #print(route)
            find_path(n, route + [n], K)

# 주어진 정보를 읽자
N, M, K, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 문제 조건에서, 최단거리가 K인 경로가 없으면 -1을 프린트하라고 했으므로
# 경로 있는지 없는지 표시

flag = False

adj_arr = [[0] * (N+1) for _ in range(N+1)] # NxN 0으로 가득찬 행렬
# N+1인 이유는, 도시의 번호를 인덱스로 사용하기 위해서

for edge in edges:
    adj_arr[edge[0]][edge[1]] = 1 # edge[0]에서 edge[1] 로 가는 길이 존재함을 표시

path = []
find_path(X, [], K)
# X 지점에서 K번 이내로 움직여서 갈 수 있는 경로 다 찾았음
path.remove([]) # 필요없는거 지우기~
my_dict = {i: [] for i in range(1, N+1)} # X번 도시에서 i번 도시로 가는 경로의 거리
for p in path:
    my_dict[p[-1]].append(len(p))

for k, v in my_dict.items():
    if v and min(v) == K: # 최단거리가 K인 도시 번호 프린트
        flag = True
        print(k)

if not flag: # 위의 상황 없음 -> -1 프린트
    print(-1)

'''
입력
4 4 2 1
1 2
1 3
2 3
2 4
path 출력 결과
[[2], [2, 3], [2, 4], [3]]

입력
4 3 2 1
1 2
1 3
1 4
path 출력 결과
[[2], [3], [4]]
'''