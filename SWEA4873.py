# SWEA 4873 반복문자 지우기
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

    def peek(self):
        return self.s[self.top]

    def is_empty(self):
        return self.top == -1


T = int(input())

for test in range(1, T+1):
    my_str = input()
    stack = Stack(len(my_str))

    for char in my_str:
        if stack.peek() == char:
            stack.pop()
        else:
            stack.push(char)

    print(f'#{test} {stack.top+1}')