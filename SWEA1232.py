# SWEA 1232 사칙연산

def postorder(n):
    if n: # n이 0이 아니면
        postorder(ch1[n])
        postorder(ch2[n])
        stack.append(my_list[n])

for test in range(1, 11):
    N = int(input())
    ch1 = [0] * (N+1) # 왼쪽 자식
    ch2 = [0] * (N+1) # 오른쪽 자식
    my_list = [0] * (N+1)
    for _ in range(N):
        lst = list(input().split())
        my_list[int(lst[0])] = lst[1]
        if len(lst) > 2:
            ch1[int(lst[0])] = int(lst[2])
        if len(lst) > 3:
            ch2[int(lst[0])] = int(lst[3])

    stack = []
    postorder(1)

    stack2 = []
    for s in stack:
        if s in ['-','+','*','/']:
            op1 = stack2.pop()
            op2 = stack2.pop()
            if s == '-':
                stack2.append(op2 - op1)
            elif s == '+':
                stack2.append(op2 + op1)
            elif s == '*':
                stack2.append(op2 * op1)
            elif s == '/':
                stack2.append(op2 / op1)
        else:
            stack2.append(int(s))

    result = int(stack2.pop())
    print(f'#{test} {result}')