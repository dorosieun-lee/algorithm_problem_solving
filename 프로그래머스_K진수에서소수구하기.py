# 프로그래머스 K진수에서 소수 개수 구하기

import math
def is_prime(number):
    if number == 1:
        return False

    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False

    return True


def transform_toK(number, k):
    my_str = ''
    while number > 0:
        my_str += str(number % k)
        number //= k
    return my_str[::-1]


def solution(n, k):
    number = transform_toK(n, k)
    num_list = number.split('0')
    answer = 0
    for n in num_list:
        if n and is_prime(int(n)):
            answer += 1

    return answer

print(solution(110011, 10))

