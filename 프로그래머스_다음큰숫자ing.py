# 프로그래머스 다음 큰 숫자

# 이진수로 변환했을 때, n과 1의 개수가 같고 n보다는 큰 수인 가장 작은 수 찾기
# 1의 개수가 같은 이진수 가능한거 다 만들어서
# n보다 크면서 가장 작은거 만들기?



def solution(n):
    def make_binary_list(i, n, bin_str, length):
        if i == n or len(bin_str) == length:
            if i == n:
                bin_list.append(bin_str + '0' * (length - len(bin_str)))
            return

        make_binary_list(i + 1, n, bin_str + '1', length)
        make_binary_list(i, n, bin_str + '0', length)

    n_bin = bin(n)
    cnt_one = n_bin.count('1')
    length = len(n_bin) - 2
    if cnt_one == length:
        length += 1
    bin_list = []
    make_binary_list(0, cnt_one-1, '1', length)
    # print(bin_list)
    answer = float("inf")
    for b in bin_list:
        num = int(b, 2) # 이진수를 십진수로 바꿈
        if n < num:
            answer = min(num, answer)

    return answer

n = 15
print(solution(n))