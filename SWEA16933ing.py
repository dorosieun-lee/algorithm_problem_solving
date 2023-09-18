# SWEA 16933 이진 탐색
# 재귀 말고 반복으로 풀어야함
# 나중에 다시 해보기
def binary_search(start, end, key):
    global result, is_left, is_right
    mid = (start + end) // 2
    if N_lst[mid] == key:
        result += 1
        return
    elif N_lst[mid] < key:
        if is_right:
            return
        is_right = True
        binary_search(mid+1, end, key)
    else:
        if is_left:
            return
        is_left = True
        binary_search(start, mid-1, key)


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    N_lst = sorted(list(map(int, input().split()))) # A
    M_lst = list(map(int, input().split())) # B

    result = 0
    for b in M_lst:
        is_left = is_right = False
        binary_search(0, N-1, b)

    print(f'#{test} {result}')