# Baekjoon 2578 빙고
numbers = [list(map(int, input().split())) for _ in range(5)]
call_nums = []
for _ in range(5):
    call_nums.extend(list(map(int, input().split())))

result = 0
for idx, n in enumerate(call_nums):
    # 숫자가 불리면, numbers에서 찾아서 그 숫자칸은 0으로 바꿈
    # 빙고가 있는지 확인
    # 이렇게 하면 O(n**2)를 두번 하게 됨.
    # 근데 5x5로 규정되어 있어서 괜찮을 듯.
    for i in range(5):
        for j in range(5):
            if numbers[i][j] == n:
                numbers[i][j] = 0

    if idx >= 11: # 숫자가 12개 미만으로 불렸으면 빙고 있는지 확인할 필요가 없음
        r_diag_cnt = 0
        l_diag_cnt = 0
        r_cnt_list = []
        c_cnt_list = []
        for i in range(5):
            r_cnt = 0
            c_cnt = 0
            if numbers[i][i] == 0:
                r_diag_cnt += 1
            if numbers[i][4-i] == 0:
                l_diag_cnt += 1

            for j in range(5):
                # 열 검사
                if numbers[i][j] == 0:
                    c_cnt += 1
                # 행 검사
                if numbers[j][i] == 0:
                    r_cnt += 1
            r_cnt_list.append(r_cnt)
            c_cnt_list.append(c_cnt)

            lst = r_cnt_list+c_cnt_list+[r_diag_cnt]+[l_diag_cnt]
            if lst.count(5) >= 3:
                result = idx
                break

    if result:
        break

# for line in numbers:
#     print(line)
print(result+1)