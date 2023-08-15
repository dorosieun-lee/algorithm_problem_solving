# SWEA 1222 계산기1

def transform(N, before):
    stack = [0] * N
    top = -1
    after = ''
    for x in before:
        if x != '+':
            after += x
        else:
            if top == -1:
                top += 1
                stack[top] = x
            else:
                after += stack[top]
                top -= 1
                top += 1
                stack[top] = x
    after += stack[top]
    return after


def calculate(N, after):
    stack = [0] * 100
    top = -1
    for x in after:
        if x != '+':
            top += 1
            stack[top] = int(x)
        else:
            a = stack[top]
            top -= 1
            b = stack[top]
            top -= 1
            top += 1
            stack[top] = a + b

    return stack[top]


for test in range(1, 11):
    N = int(input())
    before = input()
    after = transform(N, before)
    result = calculate(N, after)

    print(f'#{test} {result}')