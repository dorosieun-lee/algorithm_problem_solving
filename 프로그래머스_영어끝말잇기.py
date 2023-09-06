# 프로그래머스 영어 끝말 잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    divide = [[] for _ in range(n)]
    i = 0
    while i < len(words):
        divide[i%n].append(words[i])
        i += 1
    said = []
    answer = []
    # print(divide)
    idx = 0
    while True:
        for j in range(n):
            try:
                if idx == 0 and j == 0:
                    last = divide[j][idx]
                    said.append(divide[j][idx])
                else:
                    # print(last, divide[j][idx])
                    if last[-1] != divide[j][idx][0]:
                        answer = [j+1, idx+1]
                        break
                    if divide[j][idx] in said:
                        answer = [j+1, idx+1]
                        break
                    last = divide[j][idx]
                    said.append(divide[j][idx])
            except:
                answer = [0, 0]

        idx += 1
        if answer:
            break

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather",
 "refer", "reference", "estimate", "executive"]
print(solution(n, words))

'''
다른 사람 풀이
깔끔함...

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
'''