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
    print(after)
    #print(after)
    result = calculate(after)
    print(f'#{test} {result}')

'''
강사님 풀이

어차피 연산자는 +, * 뿐이다. 
이 경우에는 무조건 * 연산이 먼저 된다
따라서 *만 후위표기식으로 변경해서 계산해서 그 수를 다 스택에 넣고
그 후에 덧셈 연산자 수만큼 덧셈 반복하면 됨

T = 10

for t in range(1, T+1):
    input()
    STR = input()

    STACK = []
    postfix = ''

    for s in STR:
        #숫자인경우 후위표기식에 추가
        if s.isdecimal():
            postfix += s
        else: #연산자 인경우
            while STACK and STACK[-1] == '*': #스택의 연산자가 *이면 높거나 같다
                postfix += STACK.pop()
            STACK.append(s) #현재 연산자를 스택에 추가

    while STACK:
        postfix += STACK.pop()

    print(postfix)
    result = []

    for p in postfix:
        if p.isdecimal():
            result.append(int(p))
        else:
            num2 = result.pop()
            num1 = result.pop()
            if p == '+':
                result.append(num1 + num2)
            elif p == '*':
                result.append(num1 * num2)


    print(f'#{t}', *result)
'''