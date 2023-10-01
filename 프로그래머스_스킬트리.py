# 프로그래머스 스킬 트리
# 가능한 스킬트리의 개수를 반환

def is_possible(skill_stack, skill):
    tmp = skill_stack[:]
    for s in skill:
        if s in tmp and s == tmp[0]:
            tmp.pop(0)
            continue
        elif s not in skill_stack:
            continue
        else:
            return False
    return True


def solution(skills, skill_trees):
    answer = 0
    skill_stack = list(skills)
    for skill in skill_trees:
        if is_possible(skill_stack, skill):
            # print(skill)
            answer += 1

    return answer

skills = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skills, skill_trees))