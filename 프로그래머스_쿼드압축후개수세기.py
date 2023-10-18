# 프로그래머스 쿼드압축 후 개수 세기

one_cnt = 0
zero_cnt = 0

def is_same_number(arr):
    flag = arr[0][0]
    row = 0
    while row < len(arr):
        for col in range(len(arr)):
            if flag != arr[row][col]:
                return False
        row += 1
    return True


def solution(arr):
    global one_cnt, zero_cnt
    if len(arr) == 1 and type(arr[0]) == int:
        if arr[0] == 0:
            return [1, 0]
        else:
            return [0, 1]

    if len(arr) == 1:
        if arr[0][0] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
        return [zero_cnt, one_cnt]

    if is_same_number(arr):
        if arr[0][0] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
        return [zero_cnt, one_cnt]

    up = arr[0:len(arr)//2]
    down = arr[len(arr)//2:]

    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    for i in range(0, len(arr)//2):
        arr1.append(up[i][0:len(arr)//2])
        arr2.append(up[i][len(arr)//2:])
        arr3.append(down[i][0:len(arr)//2])
        arr4.append(down[i][len(arr)//2:])

    solution(arr1)
    solution(arr2)
    solution(arr3)
    solution(arr4)

    answer = [zero_cnt, one_cnt]
    return answer




arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [0]
arr = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

print(solution(arr))

'''
다른 사람 풀이
solution 함수를 마치 main.py 처럼 사용.
내부에 answer라는 변수를 만들고, check 함수도 solution 함수 내부에서 정의함

def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer
'''



