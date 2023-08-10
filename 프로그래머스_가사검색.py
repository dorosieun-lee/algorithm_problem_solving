# 프로그래머스 2020 카카오 blind recruitment 가사 검색 문제
# 정확도 테스트 통과, 효율성 테스트 2/5 통과 -> 효율성을 높혀야 함

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# 이진탐색 사용 X
def solution1(words, queries):
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

# solution1과 똑같이 실패
def solution2(words, queries):
    answer = []
    for target in queries:
        cnt = 0

        idx = target.find("?")
        start, end = 0, idx
        if idx == 0:
            idx = target[::-1].find("?")
            start, end = len(target) - idx, len(target)

        print(start, end)

        for word in words:
            if len(target) == len(word) and word[start:end] == target[start:end]:
                cnt += 1
        answer.append(cnt)

    return answer

# 이진탐색 사용
def solution3(words, queries):
    answer = []
    for target in queries:
        cnt = 0

        idx = target.find("?")
        start, end = 0, idx
        if idx == 0:
            idx = target[::-1].find("?")
            start, end = len(target) - idx, len(target)


def str_binary_search(words, start, end, key):
    mid = (start + end) // 2
    while start <= end:
        if words[mid] == key:
            return

print(solution2(words, queries))

# words 를 정렬하고 이진 탐색 알고리즘처럼 중간값을 queries랑 비교해볼까..?