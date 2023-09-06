# 프로그래머스 짝지어 제거하기
from collections import deque

def solution(my_str):
    stack = deque()
    stack.append(my_str[0])
    for s in my_str[1:]:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    if not stack:
        answer = 1
    else:
        answer = 0

    return answer

print(solution('cdcd'))