# 프로그래머스 2020 카카오 blind recruitment 가사 검색 문제
# 정확도 테스트 통과, 효율성 테스트 2/5 통과 -> 효율성을 높혀야 함

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    answer = []
    for target in queries:
        cnt = 0
        is_question = [0] * len(target)

        for i in range(len(target)):
            if target[i] == "?":
                is_question[i] += 1

        start = is_question.index(0)
        end = len(target) - is_question[::-1].index(0)

        for word in words:
            if len(target) == len(word) and word[start:end] == target[start:end]:
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(words, queries))