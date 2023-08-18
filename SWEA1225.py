# SWEA1225 암호생성기
# 원형 큐의 개념으로, 인덱스를 회전시켜서 풀이함

while True:
    try:
        tc = int(input())
        nums = list(map(int, input().split()))
    except:
        break

    lst = [0] * (8+5)
    lst[:8] = nums[:]

    zero_flag = 0
    front = 0
    rear = 8
    while True:
        for cnt in range(1, 6): # 한 사이클
            if lst[front] - cnt <= 0:
                # lst[front] - cnt 가 0보다 작은 수가 되면 = lst[rear]는 0을 저장하고, zero_flag 바꿔주고 반복문 종료
                lst[rear] = 0
                zero_flag = 1
                # 인덱스 한칸씩 밀어줌(중요!)
                front = (front + 1) % 13
                rear = (rear + 1) % 13
                break
            else:
                lst[rear] = lst[front] - cnt
                front = (front+1) % 13
                rear = (rear+1) % 13

        if zero_flag:
            if front < rear:
                result = lst[front:rear]
            else:
                result = lst[front:] + lst[:rear]

            break

    print(f'#{tc}', *result)

'''
강사님 코드
queue의 enqueue, dequeue를 이용해서 훨씬 간결함

def makePw(pw):
    while True:
        for i in range(1,6):
            num = pw.pop(0)
            pw.append(num - i)

            if pw[-1] <= 0:
                pw[-1] = 0
                return pw
                
for _ in range(1, 11):
    t = int(input())
    pw = list(map(int,input().split()))
    result = makePw(pw)
    print(f'#{t}', *result)
'''
