# Baekjoon 11052 카드 구매하기

# 카드 N개를 구매하기 위해 지불해야하는 금액의 최댓값을 구해라
# 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같다.
"""
import sys

def combination(cards, s, n):
    if cards == n:
        print(counts)
        tmp = 0
        for i, c in enumerate(counts):
            tmp += prices[i] * c
        total_price.append(tmp)
        return
    elif cards > n:
        return
    elif n - cards < s:
        return

    for i in range(s, n):
        counts[i] += 1
        combination(cards + (i + 1), i, n)
        counts[i] -= 1


N = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))
counts = [0] * N
total_price = []

combination(0, 0, N)

print(max(total_price))
"""

# DP로 푼다면?!
# 2부터, 자신이 가질 수 있는 최댓값을 저장해서 N까지 올라감 -> 구해야하는 경우의 수가 줄어듬
N = int(input())
prices = [0] + list(map(int, input().split()))

for i in range(2, N+1):
    MAX = 0
    for j in range(0, i//2+1):
        #print(j, i-j)
        MAX = max(prices[j] + prices[i-j], MAX)

    prices[i] = MAX

print(prices[-1])