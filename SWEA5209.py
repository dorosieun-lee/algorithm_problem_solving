# SWEA 5209 최소 생산 비용

def DFS(product, price):
    global MIN
    if product == N-1:
        MIN = min(MIN, price)
    if price > MIN:
        return

    for i in range(N):
        if not done[i]:
            done[i] = True
            DFS(product + 1, price + V_MAP[product+1][i])
            done[i] = False


T = int(input())
for test in range(1, T+1):
    N = int(input())
    V_MAP = [list(map(int, input().split())) for _ in range(N)]

    done = [False] * N
    MIN = float("inf")
    DFS(-1, 0)

    result = MIN
    print(f'#{test} {result}')