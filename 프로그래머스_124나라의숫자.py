# 프로그래머스 124 나라의 숫자

def solution(n):
    my_dict = {1: '1', 2: '2', 3: '4'}
    if n in my_dict.keys():
        return my_dict[n]

    answer = ''
    main = n
    while main > 0:
        remain = main % 3
        if remain == 0:
            answer = my_dict[3] + answer
            main = main - 3
        else:
            answer = my_dict[remain] + answer
            main = main - remain  # 3의 배수

        main = main // 3  # 3으로 나눈 몫

    return answer


for n in range(0, 25):
    print(n, ': ', solution(n))
