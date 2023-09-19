# SWEA 1952 수영장

def calc(n, s):
    global MIN
    if n >= 11:
        MIN = min(MIN, s)
    else:
        calc(n+1, s + prices[0] * plan[n+1])
        flag = 1 if plan[n+1] != 0 else 0
        calc(n+1, s + prices[1] * flag)
        calc(n+3, s + prices[2])


T = int(input())

for test in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    MIN = prices[3]
    calc(-1, 0)

    print(f'#{test} {MIN}')
