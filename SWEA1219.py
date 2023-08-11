# SWEA 1219 길찾기

# 방향성이 있고, 갈림길은 최대 2개
# 길 존재: 1, 존재X : 0

def dfs(start, end, nodes, adj_dict):
    stack = [start]
    visited = [0] * nodes
    visited[start] = 1
    n = start
    while True:
        if n == end:
            return 1

        for w in adj_dict[n]:
            if visited[w] == 0:
                n = w
                stack.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    if visited[end] == 1:
        return 1
    else:
        return 0


while True: # test case 갯수가 주어지지 않은 줄 알았는데..! 문제에 10개라고 주어져있었음. 문제 잘 읽기
    try:
        tc, N = list(map(int, input().split()))
        path = list(map(int, input().split()))
    except:
        break

    adj_dict = {i: [] for i in range(100)}

    for i in range(N):
        start = path[i*2]
        end = path[i*2+1]
        adj_dict[start].append(end)

    print(f'#{tc} {dfs(0, 99, 100, adj_dict)}')


"""
강사님 코드

재귀함수 사용
def dfs(vertex):
    visited[vertex] = True
    for i in path[vertex]:
        if visited[i] == False:
            dfs(i)
        # 이 문제는 99번 vertex에 방문하기만 하면 되므로
        if visited[-1] == True:
            return 
            # dfs 함수 실행 횟수를 줄일 수 있음
            
for _ in range(10):
    t, edges = map(int, input().split())
    arr = list(map(int, input().split())
    
    visited = [False] * 100
    path = [[] for _ in range(100)]
    
    for i in range(edges):
        path[arr[i*2]].append(arr[i*2+1])
        
    dfs(0)
    
    result = int(visited[-1])
    
    print(f'#{t} {result}')
    

그래프를 뒤집어서 생각해보자!
약간 더 빨라짐..!
왜...?
시작점에서 이어지는 길의 가짓수보다 도착점에서 올라가는 길의 가짓수가 적다.
항상?

def dfs(vertex):
    visited[vertex] = True
    for i in path[vertex]:
        if not visited[i]:
            dfs(i)
        # 이 문제는 0번 vertex에 방문하기만 하면 되므로
        if visited[0] == True:
            return 
            # dfs 함수 실행 횟수를 줄일 수 있음

for _ in range(10):
    t, edges = map(int, input().split())
    arr = list(map(int, input().split())
    
    visited = [False] * 100
    path = [[] for _ in range(100)]
    
    for i in range(edges): # 화살표 방향 반대로 바꿈 (도착지 -> 출발지)
        path[arr[i*2+1]].append(arr[i*2]) # 출발지 리스트 추가
        
    dfs(99)
    
    result = int(visited[0])
    
    print(f'#{t} {result}')
"""