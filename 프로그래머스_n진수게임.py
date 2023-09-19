# 프로그래머스 n진수 게임

my_dict = {0: 0, 1: 1, 2: 2,
           3: 3, 4: 4, 5: 5,
           6: 6, 7: 7, 8: 8,
           9: 9, 10: 'A',
           11: 'B', 12: 'C',
           13: 'D', 14: 'E',
           15: 'F'}
def ten_to_N(number, N):
    my_lst = []
    while number >= N:
        my_lst.append(my_dict[number % N])
        number //= N
    my_lst.append(my_dict[number % N])
    return my_lst[::-1]


def solution(n, t, m, p):
    answer = ''
    number = 0
    n_list = []
    index = p-1 # 구해야하는 수의 순서에 해당하는 index
    while True:
        n_list.extend(ten_to_N(number, n))
        if len(n_list) > index:
            answer += str(n_list[index])
            index += m
            if len(answer) >= t:
                break

        number += 1
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))