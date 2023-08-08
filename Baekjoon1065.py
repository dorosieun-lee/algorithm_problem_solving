# Baekjoon 1065 한수

N = int(input())


def digit(number):
    result = []
    while number >= 10:
        result.append(number % 10)
        number //= 10

    result.append(number)
    return result[::-1]


def is_Hansu(digit):
    diff = digit[0] - digit[1]
    for i in range(0, len(digit)-1):
        if digit[i] - digit[i+1] != diff:
            return False

    return True


cnt = 0
for i in range(1, N+1):
    if i < 10:
        cnt += 1
        continue
    digits = digit(i)

    if is_Hansu(digits):
        cnt += 1

print(cnt)
