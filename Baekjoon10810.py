N, M = map(int, input().split())
basket = ['0'] * N # 바구니

for i in range(M):
    start, end, num = map(int, input().split())
    for idx in range(start, end+1):
        basket[idx - 1] = str(num)

print(' '.join(basket))

"""    
주어진 예시 input 을 기준으로 바구니에 어떻게 담기는지.
바구니>  1     2    3    4     5
       (3)   (3)
                   (4)  (4)
        1    (1)    1    1    
              2
"""