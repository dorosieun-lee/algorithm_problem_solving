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
                print(total)
                lst += [num_list[j]]
            elif total >= n:
                if total == sum:
                    print(lst)
                    answer += 1
                break

    return answer

n = 15
print(solution(n))
