T = int(input())

for test in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5 # 지수 a,b,c,d,e 카운트

    for i in range(5):
        num = N
        while True:
            if num >= prime[i] and num % prime[i] == 0:
                num //= prime[i]
                cnt[i] += 1
            else: # 소수가 인수가 아니면 while 문에서 나가서 다음 소수로 넘어감
                break


    print(f'#{test}', *cnt)