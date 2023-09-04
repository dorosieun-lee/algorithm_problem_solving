# 프로그래머스 숫자의 표현

def solution(n):
    num_list = list(range(1, n+1))
    answer = 0
    for i in range(n):
        total = num_list[i]
        lst = [num_list[i]]
        for j in range(i+1, n):
            if total < n:
                total += num_list[j]
                lst += [num_list[j]]
                if total == n:
                    print(lst)
            elif total > n:
                break


    return answer

n = 15
print(solution(n))
