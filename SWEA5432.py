# SWEA 5432 쇠막대기 개수
# 시간초과 -> 시간 단축 어떻게??

#  - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
#  - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
#  - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
#  - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 괄호가 열리자 마자 닫히는게 아니면, 쇠막대기다
# 괄호가 열리자 마자 닫히면, 레이저다
#
# 쇠막대기 안에 레이저가 몇 개 존재하는지 세기
#


"""
T = int(input())

for test in range(1, T+1):
    my_str = input()

    razer_idx = []
    pipe_idx = {}

    for i in range(len(my_str)-1):
        if my_str[i] + my_str[i+1] == '()':
            razer_idx.append(i)
            razer_idx.append(i+1)

    cnt = 0
    cnt_stack = []

    lst = list(set(range(len(my_str))) - set(razer_idx))
    for i in lst:
        if my_str[i] == '(':
            cnt += 1
            cnt_stack.append(cnt)
            pipe_idx[cnt] = [i]

        if my_str[i] == ')':
            pipe_idx[cnt_stack.pop()].append(i)

    pipe_cnt = 0
    for key, value in pipe_idx.items():
        razer_cnt = 0
        for i in razer_idx[::2]:
            if i > value[0] and i < value[1]:
                razer_cnt += 1

        pipe_cnt += razer_cnt + 1

    print(f'#{test} {pipe_cnt}')
"""

# 레이저 입장에서 생각해보자.
# 레이저가 존재하는 시점의 왼쪽에 열린 괄호 갯수만큼 쇠막대기가 생긴다
# 잘린 쇠막대기 개수: 괄호 열리면 +1, 닫히면 +1
# 쌓여있는 쇠막대기 개수: 괄호 열리면 +1, 닫히면 -1

# ( => cnt += 1 (쇠막대기 개수 +1)
# () => ans += cnt (쌓인 쇠막대기 수만큼 잘린 조각 추가됨)
# ) => ans += 1, cnt -= 1

T = int(input())

for test in range(1, T+1):
    my_str = input()

    pipes = 0
    total = 0
    for i in range(len(my_str)-1):
        if my_str[i:i+2] == '()':
            total += pipes
        elif my_str[i] == '(':
            # print('open',i)
            pipes += 1
        elif my_str[i] == ')':
            if my_str[i-1] != '(':
                # print('close',i)
                total += 1
                pipes -= 1

    total += 1

    print(f'#{test} {total}')