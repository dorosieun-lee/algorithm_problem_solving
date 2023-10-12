# 프로그래머스 2개 이하로 다른 비트

'''
실패한 코드 -> 시간초과남
def bit_check(n, tmp):
    XOR = bin(n ^ tmp)
    if XOR.count('1') in [1, 2]:
        return True
    return False

def solution(numbers):
    answer = [0] * len(numbers)
    for i, n in enumerate(numbers):
        tmp = n
        while True:
            tmp += 1
            if bit_check(n, tmp):
                print(bin(n)[2:], '->', bin(tmp)[2:])
                answer[i] = tmp
                break
    return answer

print(solution([19, 21, 23]))
'''


def solution(numbers):
    answer = [0] * len(numbers)
    for i, n in enumerate(numbers):
        if n % 2 == 0:
            answer[i] = n + 1
            continue
        elif bin(n).count('1') == len(bin(n))-2: # 비트 전체가 1로 이루어진 수
            tmp = int('10'+bin(n)[3:], 2)
            answer[i] = tmp
            continue
        else:
            bit = bin(n)[2:]
            idx = len(bit) - bit[::-1].index('0') - 1
            tmp = bit[:idx] + '10' + bit[idx+2:]
            answer[i] = int(tmp, 2)

    return answer

print(solution([19, 21, 23]))


