# SWEA 16522 Forth

T = int(input())


def check(formula):
    stack = []
    if len(formula) == 1:
        return False
    if formula.index('.') != len(formula) - 1:
        return False

    for f in formula[:-1]:
        if f not in '+-*/':
            stack.append(f)
        else:
            try:
                stack.pop()
                stack.pop()
                stack.append('a')
            except:
                return False
    if len(stack) != 1:
        return False
    else:
        return True


for test in range(1, T+1):
    formula = list(input().split())
    stack = [0] * len(formula)
    top = -1

    if not check(formula):
        print(f'#{test} error')

    else:
        for f in formula:
            if f not in '+-*/.':
                top += 1
                stack[top] = int(f)
            elif f in '+-*/':
                a = stack[top]
                top -= 1
                b = stack[top]
                top -= 1
                if f == '+':
                    top += 1
                    stack[top] = b + a
                elif f == '*':
                    top += 1
                    stack[top] = b * a
                elif f == '-':
                    top += 1
                    stack[top] = b - a
                elif f == '/':
                    top += 1
                    stack[top] = int(b / a)
            else: # f == '.' 인 경우
                result = stack[top]

        print(f'#{test} {result}')

