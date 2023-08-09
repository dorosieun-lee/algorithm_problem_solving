# 프로그래머스 최솟값 만들기

def solution(A, B):
    A.sort()
    B.sort()
    case1 = 0
    case2 = 0
    for i in range(len(A)):
        case1 += A[i] * B[len(B)-i-1]
        case2 += B[i] * A[len(A)-i-1]

    return min(case1, case2)

A = [1,2]
B = [3,4]
print(solution(A, B))

A = [1,4,2]
B = [5,4,4]
print(solution(A, B))