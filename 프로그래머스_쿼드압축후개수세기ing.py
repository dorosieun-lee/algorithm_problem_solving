# 프로그래머스 쿼드압축 후 개수 세기
import itertools

def compress(arr, zero_cnt, one_cnt):
    print(list(itertools.chain(*arr)))
    if len(set(list(itertools.chain(*arr)))) == 1:
        if arr[0] == 1:
            zero_cnt += 1
            return
        else:
            one_cnt += 1
            return

    N = len(arr)
    areas = [[0, 0, N//2-1, N//2-1], [0, N//2, N//2-1, N-1], [N//2, 0, N-1, N//2-1], [N//2, N//2, N-1, N-1]]
    for area in areas:
        sub_arr = []
        for row in range(area[0], area[1]+1):
            sub_arr.append(arr[row][area[2]:area[3]+1])
        compress(sub_arr, zero_cnt, one_cnt)


def solution(arr):
    zero_cnt, one_cnt = 0, 0
    compress(arr, zero_cnt, one_cnt)

    answer = [zero_cnt, one_cnt]
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))