# SWEA 5097 회전문제
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    pointer = M % N
    print(f'{test} {nums[pointer]}')