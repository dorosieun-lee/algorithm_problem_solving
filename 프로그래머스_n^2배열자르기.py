# 프로그래머스 n^2 배열 자르기
# 이차원 리스트를 생성, 순회하지 않는게 포인트!

def solution(N, left, right):
    answer = [0] * (right-left+1)
    for idx, num in enumerate(range(left, right+1)):
        answer[idx] = max(num//N, num%N) + 1 # 행번호: N으로 나눈 몫, 열번호: N으로 나눈 나머지
    return answer


n, left, right = 3, 2, 5
print(solution(n, left, right))