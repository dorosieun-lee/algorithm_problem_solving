def make_list(number):
    my_str = str(number)
    my_list = list(map(int, my_str))
    if len(my_list) == 1:
        my_list = [0] + my_list
    return my_list


org_num = int(input())
test_num = org_num
cnt = 0

while True:
    num = make_list(test_num)
    #print(num)
    new_num = int(str(num[1]) + str(sum(num))[-1])
    #print(new_num)
    cnt += 1
    if new_num == org_num:
        break
    else:
        test_num = new_num

print(cnt)