# SWEA 1865 동철이의 일 분배

def DFS(person, percentage, left_max):
    global MAX
    if person == N-1:
        MAX = max(percentage, MAX)
    if percentage < MAX or percentage == 0:
        return
    if percentage * left_max < MAX:
        return

    for work in range(N):
        if not done[work]:
            done[work] = True
            DFS(person+1, percentage * P[person+1][work]/100, left_max / max_P[work])
            done[work] = False


T = int(input())
for test in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    max_P = [] # 각 열(일의 번호)의 최대 확률
    left_max = 1
    for col in zip(*P):
        max_P.append(max(col)/100)
        left_max *= max(col)/100

    #print(max_P)

    done = [False] * N # 열은 일의 번호를 의미하고, 이미 한 일은 하지 않는다.
    MAX = 0
    DFS(-1, 1, left_max)
    print(f'#{test} {MAX * 100:0.6f}')
