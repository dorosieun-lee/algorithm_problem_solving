# 프로그래머스 이진 변환 반복하기
def solution(s):
    zero_cnt = 0
    trans_cnt = 1
    while True:
        if s == "1":
            break
        s, cnt = remove_zero(s)
        zero_cnt += cnt
        if s == "1":
            break
        s = to_binary(len(s))
        trans_cnt += 1

    return trans_cnt, zero_cnt


def remove_zero(s):
    result = ''
    cnt = 0
    for char in s:
        if char != '0':
            result += char
        else:
            cnt += 1

    return result, cnt


def to_binary(num):
    bin = []
    while num >= 2:
        bin.append(num % 2)
        num //= 2
    bin.append(num)
    return ''.join(map(str, bin[::-1]))


s = "01110"
print(solution(s))
s = "01110"
print(solution(s))
s = "1111111"
print(solution(s))

