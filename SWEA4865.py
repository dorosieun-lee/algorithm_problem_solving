# SWEA 4865 글자수 세기

T = int(input())

for test in range(1, T+1):
    str1 = set(list(input()))
    str2 = input()

    count = []
    for s in str1:
        cnt = 0
        for char in str2:
            if char == s:
                cnt += 1

        count.append(cnt)

    print(f'#{test} {max(count)}')

"""
# 강사님 풀이
# 딕셔너리 사용
T = int(input())

for test in range(1, T+1):
    str1 = set(input()) # 중복된 철자 제거
    str2 = input()

    # str1의 철자를 DICT 딕셔너리의 key로 사용하고 기본 값으로 0을 줌
    DICT = dict().fromkeys(str1, 0)

    for s1 in str1:
        for s2 in str2:
            if s1 == s2:
                DICT[s1] += 1

    result = max(DICT.values())

    print(f'#{test} {result}')
    
# count 메서드 사용
T = int(input())

for test in range(1, T+1):
    str1 = set(input()) # 중복된 철자 제거
    str2 = input()
    lst = []
    
    for s1 in str1:
        lst.append(str2.count(s1))
        
    result = max(lst)
    
    print(f'#{test} {result}')
    
# 딕셔너리 comprehension 사용1
T = int(input())

for test in range(1, T+1):
    str1 = set(input()) # 중복된 철자 제거
    str_cnt = {s : 0 for s in str1} # key가 str1의 철자인 딕셔너리 생성
    str2 = input()
    
    for s in str2:
        if s in str_cnt:
            str_cnt[s] += 1
            
    result = max(str_cnt.values())
    
    print(f'#{test} {result}')

# 딕셔너리 comprehension 사용2       
T = int(input())

for test in range(1, T+1):
    str1 = set(input()) # 중복된 철자 제거
    str2 = input()
    dic = {w: str2.count(w) for w in str2 if w in str1} 
    # str2를 순회하면서 w가 str1에 있으면 str2의 w 갯수만큼을 w를 key로 해서 저장함
            
    result = max(dic.values())
    
    print(f'#{test} {result}')   
"""