# SWEA 4866 괄호검사

class Stack:
    top = -1

    def __init__(self, length):
        self.s = [0] * length

    def push(self, item):
        self.top += 1
        self.s[self.top] = item

    def pop(self):
        self.top -= 1
        return self.s[self.top + 1]

    def is_empty(self):
        return self.top == -1


def check_parentheses(test):
    stack = Stack(len(test))
    for t in test:
        if t in ['(','{']:
            stack.push(t)
        elif t in [')','}']:
            if stack.is_empty():
                return False
            elif t == ')':
                a = stack.pop()
                if a != '(':
                    return False
            elif t == '}':
                a = stack.pop()
                if a != '{':
                    return False

    return stack.is_empty()


T = int(input())
for test in range(1, T+1):
    test_str = input()
    print(f'#{test} {int(check_parentheses(test_str))}')