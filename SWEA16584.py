# SWEA 16584 배열 최소 합

# 완전탐색 -> 런타임 에러
def permutation(i, N):
    if i == N:
        new = lst[:]
        sub_lst.append(new)
        return
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            permutation(i+1, N)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())

for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)] # NxN 2차원 배열

    lst = list(range(N))
    sub_lst = []
    permutation(0, N)
    #print(sub_lst)
    MIN = 10 * N
    for my_list in sub_lst:
        tmp = 0
        for i in range(N):
            tmp += MAP[i][my_list[i]]
        if MIN > tmp:
            MIN = tmp

    print(f'#{test} {MIN}')

# DFS를 이용한 풀이
def search(row, SUM):
    global MIN
    if row == N:
        MIN = min(MIN, SUM)
        return
    if SUM >= MIN:
        return
    for col in range(N):
        if not visited_col[col]:
            visited_col[col] = True
            search(row+1, SUM+MAP[row][col])
            visited_col[col] = False


for test in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    MIN = float("inf")
    visited_col = [False] * N
    search(0, 0)
    print(f'#{test} {MIN}')

'''
# 강사님 풀이
# DFS 이용

def dfs(row, SUM):
    global result
    # 1순위 기저조건 설정
    if row == N: # 끝 행까지 다 보면
        if SUM < result:
            result = SUM
        return # 끝 행까지 다 봤으면 dfs를 끝내라. -> 근데 없어도 돌아감. 
        # 왜? -> if 끝난 후에 아래의 for문을 돌게 되는데, 
        # visitied[n]이 False인 곳이 없으면 dfs 더 수행하지 않기 때문
        # NxN 행렬이고 갔던 열은 다시 가지 않는다는 조건 때문에 가능한 것.

    # 백트래킹, 가지치기의 개념 추가! (효율성 up) <- 없어도 돌아감
    if SUM > result: # 현재 SUM 이 최소값으로 설정된 result를 넘어버리면, 더 돌 필요가 없음
        return

    # 2순위 순회
    for n in range(N):
        if not visited[n]:
            visited[n] = True
            dfs(row + 1, SUM + MAP[row][n])
            visited[n] = False # 위의 dfs 함수가 기저 조건을 만나서 끝나면, visited[n]을 다시 False로 돌려줌


T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 9*N # result 초기 설정: NxN 배열, 1-9사이 숫자가 들어가는 경우, 각 행에서 한 값을 골라 더했을 때 가장 큰 값
    # 또는 result = float('inf') -> 무한대라는 의미
    visited = [False] * N # 열 방문 여부 표시(동일한 열은 방문하지 않으니까)

    dfs(0, 0)

    print(f'#{test} {result}')

'''
