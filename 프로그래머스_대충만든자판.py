# 프로그래머스 대충 만든 자판

def solution(keymap, targets):
    SET = set()
    for target in targets:
        for char in target:
            SET.add(char)

    my_dict = {}
    for char in SET:
        for key in keymap:
            index = key.find(char)
            if index == -1:
                my_dict.setdefault(char, 101)
            else:
                if char in my_dict.keys():
                    my_dict[char] = min(my_dict[char], index + 1)
                else:
                    my_dict[char] = index + 1

    answer = []
    for target in targets:
        cnt = 0
        for char in target:
            if my_dict[char] == 101:
                answer.append(-1)
                break

            cnt += my_dict[char]
        else:
            answer.append(cnt)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))