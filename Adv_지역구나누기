# A형 기출
def subset(i):
    if i == N:
        lst1 = []
        lst2 = []
        for j, b in enumerate(bit):
            if b: lst1.append(v_list[j])
            else: lst2.append(v_list[j])
        if lst1 and lst2: # 연결되어 있는지 확인하는 것도 추가
            if (lst1 not in SUBSET) and (lst2 not in SUBSET):
                SUBSET.append(lst1)
                SUBSET.append(lst2)
    else:
        bit[i] = 1
        subset(i+1)
        bit[i] = 0
        subset(i+1)


def BFS(lst):
    if len(lst) == 1:
        return True

    q = [lst[0]]
    visited = [False] * N
    while q:
        n = q.pop()
        for w in range(N):
            if adj_arr[n][w] == 1 and not visited[w] and w in lst:
                q.append(w)
                visited[w] = True

    for l in lst[1:]:
        if not visited[l]:
            return False
    return True


T = int(input())
for test in range(1, T+1):
    N = int(input()) # 마을의 개수
    adj_arr = [list(map(int, input().split())) for _ in range(N)]
    P = list(map(int, input().split())) # 마을별 유권자 수

    # 나눌 수 있는 모든 경우를 살펴보자
    # 연결 되어 있는지 확인(BFS로)
    # 유권자 차이를 기록해서 최소값 출력

    v_list = list(range(0, N)) # 0부터 N-1까지 마을리스트
    bit = [0] * N
    SUBSET = []
    subset(0) # 두 지역구로 나눌 수 있는 경우의 수 다 구함

    diff = []
    for i in range(0, len(SUBSET), 2):
        if BFS(SUBSET[i]) and BFS(SUBSET[i+1]): # 다 연결되어 있으면
            vote1 = vote2 = 0
            for j in SUBSET[i]:
                vote1 += P[j]
            for j in SUBSET[i+1]:
                vote2 += P[j]
            diff.append(abs(vote1 - vote2))
            #print(SUBSET[i], SUBSET[i+1], diff)

    print(f'#{test} {min(diff)}')
