num = int(input()) # 후보의 수

my_list = [0] * num
for n in range(num):
    my_list[n] = int(input())


cnt = 0


while True:
    if my_list.index(max(my_list)) == 0 and my_list[::-1].index(max(my_list)) == num - 1:
        break
    elif len(set(my_list)) == 1:
        cnt += 1
        break
    else:
        max_idx = my_list[1:].index(max(my_list[1:]))
        #print(max_idx)

        my_list[max_idx+1] -= 1
        my_list[0] += 1
        cnt += 1


print(cnt)
