# SWEA 1989 초심자의 회문검사
T = int(input())

for test in range(1, T+1):
    my_str = input()
    if len(my_str) % 2 == 0: # 단어의 길이가 짝수인 경우
        if my_str[0:len(my_str)//2] == my_str[len(my_str)//2:][::-1]:
            result = 1
        else:
            result = 0
    else: # 단어의 길이가 홀수인 경우
        if my_str[0:len(my_str)//2] == my_str[len(my_str)//2+1:][::-1]:
            result = 1
        else:
            result = 0

    print(f'#{test} {result}')