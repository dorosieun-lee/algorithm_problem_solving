# SWEA 16663 이진수
# 16진수를 2진수로 바꿔봐라
def binary(number):
    if number == 0:
        return '0000'

    bin_list = [0] * 4
    n = 4 # 최대 16
    tmp = 2 ** n

    while True:
        n -= 1
        tmp = 2 ** n
        if number - tmp >= 0:
            bin_list[n] = 1
            number -= tmp
        if number == 0:
            break

    bin_list = list(map(str, bin_list[::-1]))
    return ''.join(bin_list) # str


T = int(input())
my_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for test in range(1, T+1):
    N, my_str = input().split()
    ans = ''
    for s in my_str:
        if s in my_dic.keys():
            ans += binary(my_dic[s])

        else:
            ans += binary(int(s))

    print(f'#{test} {ans}')
