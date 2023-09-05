# 프로그래머스 다음 큰 숫자

# 이진수로 변환했을 때, n과 1의 개수가 같고 n보다는 큰 수인 가장 작은 수 찾기
# 1의 개수가 같은 이진수 가능한거 다 만들어서
# n보다 크면서 가장 작은거 만들기?

MIN = float("inf")

def make_binary_list(i, n, bin_str, length, org):
    global MIN
    if i == n or len(bin_str) == length:
        if i == n:
            bin_num = bin_str + '0' * (length - len(bin_str))
            num = int(bin_num, 2)
            print(num)
            if num > org:
                MIN = min(MIN, num)  # MIN이 안바뀜!!
        return

    make_binary_list(i + 1, n, bin_str + '1', length, org)
    make_binary_list(i, n, bin_str + '0', length, org)


def solution(n):
    global MIN
    n_bin = bin(n)
    cnt_one = n_bin.count('1')
    length = len(n_bin) - 2
    if cnt_one == length:
        length += 1
    make_binary_list(0, cnt_one-1, '1', length, n)

    return MIN

n = 15
print(solution(n))