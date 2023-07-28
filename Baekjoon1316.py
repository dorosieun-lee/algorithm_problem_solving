N = int(input())

group_word_cnt = 0
for n in range(N):
    is_group = True
    my_str = input() # input 단어 하나 씩 읽음
    char = set(my_str) # 단어에서 중복되는 문자를 제외한 결과
    for c in char: # 철자를 순회
        str_cnt = my_str.count(c) # 단어 내에서 해당 문자가 몇번 나오는지 카운트. 만약 한번만 나온다면 아래의 과정 필요 없음.
        if str_cnt >= 2:
            idx_list = [] # 중복되는 문자(단어 내에서 두번 이상 존재)의 인덱스를 저장하는 리스트
            idx = 0
            # 단어를 문자 하나씩 순회하면서 해당하는 문자의 인덱스를 찾고 저장
            for s in my_str:
                idx += 1
                if c == s:
                    idx_list.append(idx)
            #print(idx_list)
            # 단어 내 중복되는 문자의 인덱스끼리 비교. 바로 옆이면 그룹 단어에 해당
            # 인덱스의 차이가 1 초과이면 그룹 단어 아님
            for i, j in enumerate(idx_list):
                if i == 0:
                    a = j # 문자가 처음 나오는 인덱스
                else:
                    b = a # 문자의 인덱스 중 앞의 것
                    a = j # 문자의 인덱스 중 뒤의 것
                    if abs(a - b) > 1: # 둘의 차이가 1 초과이면 그룹 단어가 아님
                        is_group = False

    if is_group: # 그룹 단어일 때만 group_word_cnt + 1
        group_word_cnt += 1

print(group_word_cnt)