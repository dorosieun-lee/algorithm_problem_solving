# 프로그래머스 타겟 넘버

def solution(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            numbers[i+j] = numbers[i+j] * (-1)

    answer = 0
    return answer

적절히 더하고 뺀다........
적절히
4 1 2 1
4
-1 하나만 곱해서 다 sum해보기
-1 두개 숫자에 곱해서 sum
...
-1 개수를 숫자 개수만큼