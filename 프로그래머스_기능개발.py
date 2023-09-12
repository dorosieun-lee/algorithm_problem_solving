# 프로그래머스 기능개발

def solution(progresses, speeds):
    n = len(progresses)
    needs = [0] * n
    for i in range(n):
        needs[i] = (100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[
            i]) // speeds[i] + 1

    answer = []
    while len(needs) >= 1:
        max_idx = needs.index(max(needs))
        answer.append(len(needs) - max_idx)
        needs = needs[:max_idx]

    return answer[::-1]

print(solution([90, 98, 97, 96, 98], [1, 1, 1, 1, 1]))