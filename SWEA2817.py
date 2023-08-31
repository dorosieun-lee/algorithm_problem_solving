# SWEA 2817 부분수열의 합
def subset(i, n, init, total):
    global cnt
    if i == n:
        if total == K and init:
            cnt += 1
            return
        return

    else:
        bit[i] = 1
        subset(i+1, n, init+[lst[i]], total+lst[i])
        bit[i] = 0
        subset(i+1, n, init, total)


T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    bit = [0] * N
    subset(0, N, [], 0)

    print(f'#{test} {cnt}')