# Baekjoon 10973 이전 순열

# 사전순으로 바로 이전에 오는 순열을 구해라~~
# 가장 앞서는 순열은 오름차순, 가장 마지막 순열은 내림차순

"""
메모리 초과ㅜㅜ

from itertools import permutations as perm

N = int(input())
lst = tuple(map(int, input().split()))

ordered = sorted(list((perm(range(1, N+1)))))
index = ordered.index(lst)

if index == 0:
    print(-1)
else:
    print(*ordered[index-1])
"""

N = int(input())
lst = list(map(int, input().split()))

if lst == list(range(1, N+1)):
    print(-1)
else:
    for i in range(N-2, -1, -1):
        if lst[i:] == sorted(lst[i:]):
            continue
        else:
            tmp = lst[i:][:]
            first = 0
            for j in tmp:
                if j < tmp[0]:
                    first = max(j, first)
            tmp.remove(first)

            tmp = lst[:i] + [first] + sorted(tmp, reverse=True)
            print(*tmp)
            break


