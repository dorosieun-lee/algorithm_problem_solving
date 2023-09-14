# 프로그래머스 피로도
from itertools import permutations as perm

def solution(k, dungeons):
    perm_list = list(perm(list(range(len(dungeons))), len(dungeons)))
    MAX = 0
    for pl in perm_list:
        tired = k
        cnt = 0
        for i in pl:
            if tired >= dungeons[i][0]:
                tired -= dungeons[i][1]
                cnt += 1
            else:
                MAX = max(MAX, cnt)
                break
        else:
            MAX = max(MAX, cnt)

    return MAX

k = 80
dungeons = [[80, 20],[50, 40],[30, 10]]

print(solution(k, dungeons))