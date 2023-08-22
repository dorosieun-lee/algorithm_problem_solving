# SWEA 4837 부분집합의 합
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

# 비트 연산자를 이용한 풀이 -> 완전탐색
# 부분집합의 갯수: 1<<len(setA) (2^len(setA))
T = int(input())

for test in range(1, T+1):
    setA = list(range(1, 13))
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1<<len(setA)):
        subset = []
        for j in range(len(setA)):
            if i & (1<<j):
                subset.append(setA[j])

        if len(subset) == N and sum(subset) == K:
            #print(subset)
            cnt += 1

    print(f'#{test} {cnt}')