N = int(input())

num_list = []
while N >= 10:
    num_list.append(N % 10)
    N //= 10
num_list.append(N)

num_list.sort(reverse=True)
num_list = list(map(str, num_list))

print(''.join(num_list))