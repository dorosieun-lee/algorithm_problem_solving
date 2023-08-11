# 프로그래머스 귤 고르기

def solution(k, tangerine):
    count = [0] * max(tangerine)
    for t in tangerine:
        count[t - 1] += 1

    count.sort(reverse=True)  # 내림차순 정렬

    basket = 0
    i = 0
    answer = 0
    while basket < k:
        basket += count[i]
        i += 1
        answer += 1

    if basket >= k:
        return answer
    else:
        return answer + 1


k, tangerine = 4, [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

k, tangerine = 2, [1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, tangerine))

"""
다른 사람 풀이(by 블티) -> 신박해!

from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))

"""
