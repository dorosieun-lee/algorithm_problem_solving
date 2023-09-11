# 프로그래머스 N개의 최소공배수

def solution(arr):
    num = max(arr)
    while True:
        yes_or_no = 1
        for n in arr:
            if num % n == 0:
                yes_or_no *= 1
            else:
                yes_or_no *= 0

        if yes_or_no == 1:
            break
        else:
            num += 1

    answer = num
    return answer

arr = [2, 6, 8, 14]
print(solution(arr))