total = int(input())
N = int(input())

add_price = 0

for n in range(N):
    price, cnt = map(int, input().split())
    add_price += price * cnt

if total == add_price: print('Yes')
else: print('No')