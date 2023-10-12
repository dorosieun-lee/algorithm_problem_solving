# 프로그래머스 택배상자
from collections import deque

def solution(order):
    sub = deque() # stack
    truck = deque() # append만 함
    idx = 0 # order의 인덱스
    # 기본 컨테이너 순서대로 검사
    for box in range(1, len(order)+1):
        if box != order[idx]:
            # 보조 컨테이너 확인
            while sub:
                if sub[-1] == order[idx]:
                    truck.append(sub.pop())
                    idx += 1
                else:
                    break
            sub.append(box)
        # 기본 컨테이너 박스 번호와 order의 박스 번호가 일치하면 바로 트럭에 싣기
        else:
            truck.append(box)
            idx += 1

    # 기본 컨테이너를 모두 확인한 후에, 보조 컨테이너에 담긴 게 있는지 확인
    while sub and idx < len(order):
        if sub[-1] == order[idx]:
            truck.append(sub.pop())
            idx += 1
        else:
            break

    answer = len(truck)
    return answer

order = [5,4,3,2,1]
print(solution(order))