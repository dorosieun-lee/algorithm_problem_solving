# 프로그래머스 의상
def solution(clothes):
    my_dict = {}
    for cloth in clothes:
        my_dict[cloth[1]] = 1 + my_dict.setdefault(cloth[1], 1)

    # print(my_dict)
    answer = 1
    for v in my_dict.values():
        answer *= v

    return answer - 1