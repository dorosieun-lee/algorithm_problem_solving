# SWEA 1242 암호코드 스캔

my_dic = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
          '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9}
def bit_to_num(lst): # 56의 배수로 들어옴
    n = len(lst)//56
    num_list = []
    for i in range(0, len(lst), 7*n):
        cut_lst = lst[i:i+7*n]
        before = '0'
        cnt = 0
        tmp = ''
        for l in cut_lst:
            if before == l:
                cnt += 1
                continue
            else:
                before = l
                tmp += str(cnt//n)
                cnt = 1
        tmp += str(cnt//n)
        num_list.append(my_dic[tmp])
    return num_list

def hex_to_bin(hex_num): # 16진수를 10진수로 바꾸고 다시 2인수로 바꿈... 비효율적
    N = len(hex_num)
    hex_num = int('0x' + hex_num.lower(), 0)

    output = ""
    for j in range(N * 4 - 1, -1, -1):
        output += "1" if hex_num & (1 << j) else "0"
    return output

def check_code(code):
    num = sum(code[0::2]) * 3 + sum(code[1:-1:2]) + code[-1]
    return True if num % 10 == 0 else False


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    code_arr = [input().strip() for _ in range(N)]
    code_arr = list(set(code_arr)) # 중복제거
    #code_arr = [list(code_arr[i]) for i in range(len(code_arr))]
    #print(code_arr)

    row_idx = []
    n_row = len(code_arr)
    n_col = len(code_arr[0])
    for row in range(n_row):
        for col in range(n_col):
            if code_arr[row][col] != '0':
                row_idx.append(row)
                break

    transform = [] # 변환한 코드
    exist = []
    for row in row_idx:
        line = code_arr[row].strip('0')

        for e in exist: # 이미 처리한 코드가 들어있으면
            if e in line:
                line = line.replace(e, '0') # '0' 으로 바꿔버려~

        line = line.strip('0')

        bit = ''
        for i, s in enumerate(line[::-1]):
            tmp = hex_to_bin(s) # 16진수를 4비트 이진수로 표현
            bit = tmp + bit # 뒤에서부터 붙임

        bit = bit.strip('0') # 앞뒤 0 다 잘라줌
        # print('bit: ', bit)
        # print('len of bit: ', len(bit))
        if len(bit) < 56:
            while len(bit) < 56:
                bit = '0' + bit
            num = bit_to_num(bit)
            if num not in transform:
                transform.append(num)

        else:
            n = 1
            while len(bit) >= 56*n:
                start = len(bit) - 56*n
                try:
                    num = bit_to_num(bit[start:])
                    if num not in transform:
                        transform.append(num)
                    bit = bit[:start].strip('0')
                    n = 1
                except:
                    n += 1
                    while len(bit) < 56*n:
                        bit = '0' + bit # 앞에 0 붙여주기

            if len(bit) < 56 and set(bit) != {'0'} and start != 0: # bit가 56개 이하로 남았는데 1,0으로 이루어져 있으면
                while len(bit) < 56:
                    bit = '0' + bit
                num = bit_to_num(bit)
                if num not in transform:
                    transform.append(num)

    #print(transform)
    result = 0
    for tr in transform:
        if check_code(tr):
            result += sum(tr)

    print(f'#{test} {result}')
