# SWEA 10804 문자열의 거울상

T = int(input())

mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
for test in range(1, T+1):
    my_str = input()

    result = ''
    for s in my_str[::-1]:
        result  += mirror[s]

    print(f'#{test} {result}')