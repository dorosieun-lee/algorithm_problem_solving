# 프로그래머스 할인행사

def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - 10 + 1):
        my_dict = {item: 0 for item in want}
        yes_or_no = True
        for j in range(i, i+10):
            if discount[j] in my_dict.keys():
                my_dict[discount[j]] += 1

        print(i, my_dict)
        for k in range(len(want)):
            if my_dict[want[k]] < number[k]:
                yes_or_no = False
                break

        if yes_or_no:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))