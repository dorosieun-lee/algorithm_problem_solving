# Baekjoon 1149 RGB거리
# 다이나믹 프로그래밍!
import sys

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            MAP[i][j] += min(MAP[i - 1][j + 1], MAP[i - 1][j + 2])
        elif j == 1:
            MAP[i][j] += min(MAP[i - 1][j - 1], MAP[i - 1][j + 1])
        else:
            MAP[i][j] += min(MAP[i - 1][j - 1], MAP[i - 1][j - 2])

print(min(MAP[-1]))