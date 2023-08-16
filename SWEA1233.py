# SWEA 1223 계산기2

def transform(before):
    priority = {'+': 1, '*': 2}
    after = ''
    stack = []
    for x in before:
        if x not in '+*':
            after += x
        else:
            if not stack: # stack이 비어있으면,
                stack.append(x)
            else:
                if not stack or priority[x] > priority[stack[-1]]:
                    stack.append(x)
                elif priority[x] <= priority[stack[-1]]:
                    while stack and priority[x] <= priority[stack[-1]]:
                        after += stack.pop()
                    stack.append(x)
    while stack:
        after += stack.pop()
    return after


def calculate(formula):
    num_stack = []
    for x in formula:
        if x not in '+*':
            num_stack.append(int(x))
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            if x == '+':
                num_stack.append(b + a)
            elif x == '*':
                num_stack.append(b * a)
    #print(num_stack)
    return num_stack.pop()


for test in range(1, 11):
    N = int(input())
    before = input()
    after = transform(before)
    #print(after)
    result = calculate(after)
    print(f'#{test} {result}')