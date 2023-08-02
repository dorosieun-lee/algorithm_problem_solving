# SWEA 18132 부분집합의 합
# 부분집합 만드는 방법, 완전탐색 외의 풀이 생각해보기
T = int(input())

for test in range(1, T+1):
    setA = list(range(1, 13))
    N, K = list(map(int, input().split()))
    cnt = 0

    subsets = [[]]
    for n in setA:
        size = len(subsets)
        for y in range(size):
            subsets.append(subsets[y]+[n])

    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print(f'#{test} {cnt}')