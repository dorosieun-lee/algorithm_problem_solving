# 프로그래머스 뒤에 있는 큰 수 찾기
# 단순히 반복문을 사용하면 시간초과가 뜬다
# stack을 활용하는게 팁
from collections import deque

def solution(numbers):
    answer = []
    stack = deque()

    for n in reversed(numbers):
        while len(stack) > 0:
            if stack[-1] > n:
                answer.append(stack[-1])
                stack.append(n)
                break
            else:
                stack.pop()
        else:
            answer.append(-1)
            stack.append(n)

    return answer[::-1]

numbers = [1,2,5,4,5,6]
print(solution(numbers))

'''
다른 사람 풀이
index를 stack에 담고, 더 큰 수를 만날 때까지 while 반복문

def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result
'''