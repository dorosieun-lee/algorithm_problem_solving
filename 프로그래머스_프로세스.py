# 프로그래머스 프로세스
def solution(priorities, location):
    queue = []
    for i, p in enumerate(priorities):
        queue.append((i, p))

    cnt = 0
    while queue:
        i, p = queue.pop(0)
        if queue and max(list(zip(*queue))[1]) > p:
            queue.append((i, p))
        else:
            cnt += 1
            if i == location:
                answer = cnt

    return answer

priorities = [2,1,3,2]
location = 2
priorities = [1,1,9,1,1,1]
location = 0

print(solution(priorities, location))