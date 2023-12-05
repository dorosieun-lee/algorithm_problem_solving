# 두 큐 합 같게 만들기_프로그래머스
# sum 연산을 계속 하는 것보다 sum 변수를 만들어서 값을 하나씩 빼주는게 시간 효율성이 더 좋다
# list로 시간초과나면 무조건 deque로 변경해보자
# 필요 없는 연산을 찾아내서 제거해주자

# 이 풀이는 queue1 = [1, 10, 1, 2], queue2 = [1, 2, 1, 2] 로 하면 오답이 나옴
from collections import deque

def solution(queue1, queue2):
    if sum(queue1) + sum(queue2) % 2 == 1:
        return -1
    else:
        target_sum = (sum(queue1) + sum(queue2)) / 2

    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)

    while queue1 and queue2:
        if sum1 < target_sum:
            tmp = queue2.popleft()
            sum1 += tmp
            queue1.append(tmp) # 아래 조건에서 queue1.popleft() 해야하므로 이 과정은 필요함
            answer += 1
        elif sum1 > target_sum:
            sum1 -= queue1.popleft()
            answer += 1
        else:
            return answer

    return -1

"""
다른 풀이 
처음부터 큐를 연결시켜 놓고 빼고, 더하는 식 -> 최대 queue의 길이 * 6 번의 연산을 함

def solution(queue1, queue2):
    indicator2=sum(queue1)-int(sum(queue1+queue2)/2)
    answer=0
    sub_list=(queue1+queue2+queue1)[::-1]
    add_list=(queue2+queue1+queue2)[::-1]
    while indicator2!=0:
        try:
            if indicator2>0:
                indicator2-=sub_list.pop()
            else:
                indicator2+=add_list.pop()
        except:
            return -1
        answer+=1
    return answer
"""
queue1 = [1,10,1,2] #[1, 2, 1, 2] #[3,2,7,2]
queue2 = [1,2,1,2] #[1, 10, 1, 2] #[4,6,5,1]
print(solution(queue1, queue2))


