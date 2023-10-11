# 프로그래머스 롤케이크

def solution(topping):
    left = set()
    right = {}
    answer = 0

    for i in topping:
        right[str(i)] = right.get(str(i), 0)
        right[str(i)] += 1
    print(right)
    for i in topping:
        left.add(i)
        right[str(i)] -= 1
        if right[str(i)] == 0:
            del right[str(i)]

        if len(left) == len(right.keys()):
            answer += 1

    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]
# topping = [1,2,3,1,4]
print(solution(topping))