# SWEA 4366 정식이의 은행업무

# 2진수와 3진수를 기억하는데, 둘 다 한자리는 잘못됨
def make(origin, type):
    pos_list = []
    if type == 'binary':
        for i in range(len(origin)):
            tmp = origin[:]
            tmp[i] = '1' if tmp[i] == '0' else '0'
            pos_list.append(tmp)

        for i, n in enumerate(pos_list):
            my_str = '0b' + ''.join(n)
            pos_list[i] = int(my_str, 0)

    if type == 'ternary':
        for i in range(len(origin)):
            tmp = origin[:]
            if tmp[i] == '0':
                tmp[i] = '1'
                pos_list.append(tmp[:])
                tmp[i] = '2'
                pos_list.append(tmp[:])
            elif tmp[i] == '1':
                tmp[i] = '0'
                pos_list.append(tmp[:])
                tmp[i] = '2'
                pos_list.append(tmp[:])
            elif tmp[i] == '2':
                tmp[i] = '0'
                pos_list.append(tmp[:])
                tmp[i] = '1'
                pos_list.append(tmp[:])

        for i, n in enumerate(pos_list):
            my_str = ''.join(n)
            pos_list[i] = change_ter(my_str)

    return pos_list


def change_ter(my_str):
    number = 0
    i = 0
    for s in my_str[::-1]:
        number += 3**i * int(s)
        i += 1
    return number


T = int(input())
for test in range(1, T+1):
    binary = list(input()) # 2진수
    ternary = list(input()) # 3진수

    bin_list = make(binary, 'binary')
    ter_list = make(ternary, 'ternary')
    result = set(bin_list) & set(ter_list)
    print(f'#{test}', *result)