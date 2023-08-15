# 프로그래머스_연속 부분 수열 합의 개수
def solution(elements):
    length = len(elements)
    elements = elements * 2
    my_set = []
    subtotal = []
    for n in range(1, length+1):
        if n == 1:
            subtotal = elements[:length]
            my_set.extend(subtotal)
        else:
            for i in range(length):
                subtotal[i] += elements[i+(n-1)]
            my_set.extend(subtotal)
    return len(set(my_set))

print(solution([7,9,1,1,4]))