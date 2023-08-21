# 프로그래머스 쿼드압축 후 개수 세기

def compress(arr):
    if set(arr) == 1:
        if arr[0] == 1:
            zero_cnt += 1
        else:
            one_cnt += 1

    N = len(arr)
    areas = [[0, 0, N//2 - 1, N//2 - 1], [N//2 - 1, 0, N//2, N-1], [N//2, 0, N//2 - 1, N-1], [N//2, N//2, N-1, N-1]]
    for area in areas:
        sub_arr = []
        for i in range(area[0], area[1]+1):
            for
        compress()
def solution(arr):
    zero_cnt = 0
    one_cnt = 0
    compress(arr)

    answer = []
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]