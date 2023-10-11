# 프로그래머스 숫자 변환하기

def solution(x, y, n):
    counts = [-1] * (y+1)
    counts[x] = 0

    for i in range(x, y+1):
        if counts[i] != -1:
            if i + n <= y:
                if counts[i + n] > -1:
                    counts[i + n] = min(counts[i + n], counts[i] + 1)
                else:
                    counts[i + n] = counts[i] + 1

            if i * 2 <= y:
                if counts[i * 2] > -1:
                    counts[i * 2] = min(counts[i * 2], counts[i] + 1)
                else:
                    counts[i * 2] = counts[i] + 1

            if i * 3 <= y:
                if counts[i * 3] > -1:
                    counts[i * 3] = min(counts[i * 3], counts[i] + 1)
                else:
                    counts[i * 3] = counts[i] + 1

    answer = counts[y]
    return answer

x, y, n = 10, 40, 5
# x, y, n = 2, 5, 4
print(solution(x, y, n))