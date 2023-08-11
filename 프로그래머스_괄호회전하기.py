# 프로그래머스 괄호 회전하기

def solution(s):
    answer = 0
    for i in range(len(s)):
        rot = s[i:] + s[:i]
        if is_right(rot):
            answer += 1

    return answer


def is_right(my_str):
    stack = [0]
    for s in my_str:
        if s in ['{','[','(']:
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False

    if stack[-1] == 0:
        return True
    else:
        return False


s = "}}}"
print(solution(s))