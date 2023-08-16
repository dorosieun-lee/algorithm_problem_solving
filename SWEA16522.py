# SWEA 16522 Forth

T = int(input())

# 피연산자의 개수가 연산자의 개수보다 하나 더 많아야 계산할 수 있는 수식
'''
number, operation = 0, 0
for f in formula:
    if f.isdecimal():
        number += 1
    elif f in "+*-/":
        operation += 1
        
if number - operation == 1:
    계산 수행
else:
    print("error")
    
# -> 피연산자, 연산자 개수가 잘 맞아도 연산자가 몰려있는 경우가 있으면 잘못된 수식임 (이 코드로는 그건 못 걸러냄)
'''
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

