# 프로그래머스 카펫 문제
def solution(brown, yellow):
    total = brown + yellow
    subset = []
    for i in range(3, total // 2): # 2보다 작으면 갈색으로 둘러쌓인 노란색 카펫이 존재할 수 없으므로, 3 이상의 수를 탐색
        if total % i == 0:
            if [total // i, i] in subset: # 이미 subset에 존재하는 리스트면 추가하지 않고 반복문 종료
                break
            else:
                subset.append([i, total // i])

    for s in subset:
        if (s[0] - 2) * (s[1] - 2) == yellow: # 노란색 영역은 (가로 - 2) * (세로 - 2)에 해당함
            answer = sorted(s)[::-1] # 가로가 세로보다 길거나 같으므로 내림차순 정렬해서 역순으로(다른 방법도 가능)

    return answer