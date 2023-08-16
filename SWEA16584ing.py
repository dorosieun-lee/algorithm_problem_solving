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


def f(i, N, s):
    if i == N:
        return
    else:
        f(i+1, N, s+MAP[i])
        f(i+1, N, s)


