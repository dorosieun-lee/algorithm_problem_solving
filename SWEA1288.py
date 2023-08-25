# SWEA 1288 새로운 불면증 치료법

T = int(input())
for test in range(1, T+1):
    N = int(input())

    i = 1
    digit = set([])
    while len(digit) != 10:
        num = N * i # N의 배수
        len_num = len(str(num))
        tmp = [0] * len_num # 자릿수 (-> 순서 반대로인데, 상관없음)
        tmp_num = num
        j = 0
        while tmp_num >= 10:
            tmp[j] = tmp_num % 10
            tmp_num //= 10
            j += 1
        tmp[j] = tmp_num
        digit = digit | set(tmp)
        i += 1

    print(f'#{test} {num}')