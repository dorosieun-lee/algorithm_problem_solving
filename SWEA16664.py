# SWEA 16664 이진수2
def binary(number):
    bin_list = [0] * 12
    n = 0
    tmp = 2**((-1)*n)

    while True:
        if n >= 12:
            return 'overflow'

        n += 1
        tmp = 2 ** ((-1) * n)
        if number - tmp >= 0:
            bin_list[n-1] = 1
            number -= tmp

        if number == 0:
            break

    bin = ''.join(list(map(str, bin_list[:n])))
    return bin

T = int(input())
for test in range(1, T+1):
    F = float(input())
    bin = binary(F)
    print(f'#{test} {bin}')