# 프로그래머스 주차 요금 계산

import math
def solution(fees, records):
    answer = []
    my_dict = {}
    for record in records:
        time, N_car, _ = record.split()
        if N_car in my_dict.keys():
            my_dict[N_car].append(time)
        else:
            my_dict[N_car] = [time]

    my_list = sorted(list(my_dict.items()), key=lambda x: x[0])
    prices = []
    for N_car, times in my_list:
        if len(times) % 2 != 0:
            times.append('23:59')

        duration = 0
        for i in range(0, len(times), 2):
            diff_h = int(times[i+1][0:2]) - int(times[i][0:2])
            if int(times[i+1][3:]) >= int(times[i][3:]):
                diff_m = int(times[i+1][3:]) - int(times[i][3:])
            else:
                diff_h -= 1
                diff_m = (int(times[i+1][3:])+60) - int(times[i][3:])
            duration += diff_h * 60 + diff_m

        if duration <= fees[0]:
            price = fees[1]
        else:
            price = fees[1] + math.ceil((duration-fees[0]) / fees[2]) * fees[3]

        prices.append(price)

    return prices

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)