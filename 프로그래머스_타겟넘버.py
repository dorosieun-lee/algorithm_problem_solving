# 프로그래머스 타겟 넘버

def solution(numbers, target):
    def DFS(i, total, target):
        if i == N:
            if total == target:
                cnt.append(1)
            return
        # 가지치기
        if (total + sum(numbers[i:]) < target) or (total - sum(numbers[i:]) > target):
            return

        if not visited[i]:
            visited[i] = True
            DFS(i + 1, total + numbers[i], target)
            visited[i] = False
            DFS(i + 1, total - numbers[i], target)

    numbers.sort()
    visited = [False] * len(numbers)
    N = len(visited)
    cnt = []
    DFS(0, 0, target)

    answer = sum(cnt)
    return answer


numbers = [4, 1, 2, 1]
target = 4
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))