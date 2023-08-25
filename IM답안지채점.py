# 답안지 채점

# 정환 선생님은 학생들의 시험지를 채점하려고 한다.
# 시험은 1 부터 5 까지의 5 개의 항목 중, 정답을 선택하는 객관식으로 총 M개의 문제가 주어진다.
# 학생들이 제출한 답안지에는 각 문제에 대해 선택한 항목의 번호가 적혀 있다.
# 채점 방식은 다음과 같다.
# 정답을 맞춘 문제는 1 점이 주어진다. 연속으로 정답을 맞출 경우, 이전 점수에서 보너스 1 점이
# 가산되어 주어진다.

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    MIN = float("inf")
    MAX = 0

    for _ in range(N):
        score = 0
        add = 0
        s_ans = list(map(int, input().split())) # 학생의 답안지

        for i in range(M):
            if s_ans[i] == ans[i]:
                score += (1 + add)
                add += 1
            else:
                add = 0

        MIN = min(score, MIN)
        MAX = max(score, MAX)

    result = MAX - MIN

    print(f'#{test} {result}')

'''
강사님 코드
T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    answer = list(map(int,(input().split())))
    student = []
    score = []
    for i in range(N):
        student.append(list(map(int,(input().split()))))

    for i in range(len(student)):
        cnt = 0
        result = 0
        for j in range(len(answer)):

            if student[i][j] == answer[j]:
                cnt += 1
                result += cnt
            else :
                cnt = 0
        score.append(result)
    
    result = max(score) - min(score)

    print(f"#{t} {result}")
'''