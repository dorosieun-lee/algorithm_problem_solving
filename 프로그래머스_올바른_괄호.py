# 프로그래머스
# 올바른 괄호 문제
# stack 알고리즘 활용

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) > 0 and stack[-1] != '(':
                return False
            elif len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False

    return True

test_case = "(()("
print(solution(test_case)) # -> False