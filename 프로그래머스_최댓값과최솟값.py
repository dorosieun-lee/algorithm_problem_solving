# 프로그래머스 최댓값과 최솟값

def solution(s):
    lst = list(map(int, s.split()))
    MAX = max(lst)
    MIN = min(lst)

    answer = ' '.join(map(str, [MIN, MAX]))
    return answer

s = "1 2 3 4"
print(solution(s))
s = "-1 -2 -3 -4"
print(solution(s))
s = "-1 -1"
print(solution(s))
