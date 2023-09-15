# 프로그래머스 뉴스 클러스터링
def solution(str1, str2):
    set1 = []
    for i in range(0, len(str1) - 1):
        tmp1 = str1[i:i + 2].upper()
        if tmp1.isalpha():
            if tmp1 in set1:
                num = 1
                while True:
                    tmp2 = tmp1 + str(num)
                    if tmp2 not in set1:
                        set1.append(tmp2)
                        break
                    num += 1
            else:
                set1.append(tmp1)

    set2 = []
    for i in range(0, len(str2) - 1):
        tmp1 = str2[i:i + 2].upper()
        if tmp1.isalpha():
            if tmp1 in set2:
                num = 1
                while True:
                    tmp2 = tmp1 + str(num)
                    if tmp2 not in set2:
                        set2.append(tmp2)
                        break
                    num += 1
            else:
                set2.append(tmp1)

    print(set1, set2)
    union = len(set(set1) | set(set2))
    inter = len(set(set1) & set(set2))

    answer = 1 if union == 0 else inter / union
    return int(answer * 65536)


str1 = 'France'
str2 = 'French'
print(solution(str1, str2))

"""
파이써닉하게!
import math
from collections import Counter

def solution(str1, str2):
    set1 = Counter([str1[i:i+2].upper() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()])
    set2 = Counter([str2[i:i+2].upper() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()])
    J = lambda A, B: 1 if len(A) == 0 and len(B) == 0 else sum((A & B).values()) / sum((A | B).values())
    return math.floor(J(set1, set2) * 65536)

"""


