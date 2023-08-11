# SWEA 1234 비밀번호
class Stack:
    top = -1
    def __init__(self, length):
        self.s = [0] * length

    def push(self, item):
        self.top += 1
        self.s[self.top] = item

    def peek(self):
        return self.s[self.top]

    def pop(self):
        self.top -= 1
        return self.s[self.top + 1]

    def is_empty(self):
        return self.top == -1


T = 10

for test in range(1, T+1):
    N, pw = input().split()
    stack = Stack(len(pw))

    for n in pw:
        if stack.peek() == n:
            stack.pop()

        else:
            stack.push(n)

    # result = []
    # while not stack.is_empty():
    #     result.append(stack.pop())

    # print(f'#{test}', ''.join(result[::-1]))
    print(f'#{test}', ''.join(stack.s[:stack.top+1]))

