# SWEA 4839 이진 탐색
T = int(input())


def binary_search(l, r, key):
    cnt = 0
    while l < r:
        cnt += 1
        mid = (l+r) // 2
        if mid == key:
            return cnt
        elif mid < key:
            l = mid
        elif mid > key:
            r = mid



for test in range(1, T+1):
    P, A, B = list(map(int, input().split()))
    A_cnt = binary_search(1, P, A)
    B_cnt = binary_search(1, P, B)

    if A_cnt > B_cnt:
        win = "B"
    elif A_cnt < B_cnt:
        win = "A"
    else:
        win = 0

    print(f"#{test} {win}")