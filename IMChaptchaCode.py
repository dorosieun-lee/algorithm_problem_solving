# Captcha code

# 코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다
# (1) 랜덤으로 N개 길이의 Sample이 주어진다
# (2) 그리고 K개 길이의 PassCode가 주어진다
# (3) 사용자는 Sample에서 PassCode를 "순차적으로"만들 수 있는지를 검증해야 한다

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    result = 0
    idx = 0

    for p in passcode:
        for i in range(idx, N):
            if sample[i] == p:
                print(i)
                result = 1
                idx = i+1 # +1 해주는거 중요!!!
                break
        else:
            result = 0
            break

    print(f'#{test} {result}')

'''
강사님 코드
T = int(input())
for tc in range(1, T+1) : 
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    
    indexes = [] 
    res = 1 
    
    for i in range(len(passcode)) : 
        now = passcode[i]
        try : 
            index = sample.index(now)
            sample = sample[index:]
        except : 
            res = 0 

    print(f"#{tc} {res}")
'''