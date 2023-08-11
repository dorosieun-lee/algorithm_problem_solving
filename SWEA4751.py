# SWEA 4751 다솔이의 다이아몬드 장식
# 규칙 찾기가 포인트!

T = int(input())

for test in range(1, T+1):
    my_str = input()
    n = len(my_str)
    str_list = ['..#.', '.#.#', '#.{}.']

    for i in range(5):
        if i in [0, 4]:
            print(str_list[0] * n, end='')
            print('.')
        if i in [1, 3]:
            print(str_list[1] * n, end='')
            print('.')
        if i == 2:
            for s in my_str:
                print(str_list[2].format(s), end='')
            print('#')
