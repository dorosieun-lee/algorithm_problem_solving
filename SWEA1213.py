# SWEA 1213 String

T = 10 # test case 갯수 = 10

for test in range(1, T+1):
    input() # test case 번호
    pattern = input()
    my_str = input()
    count = 0

    for i in range(len(my_str)-len(pattern)+1):
        for j in range(len(pattern)):
            if my_str[i+j] != pattern[j]:
                break
        else:
            count += 1

    print(f'#{test} {count}')