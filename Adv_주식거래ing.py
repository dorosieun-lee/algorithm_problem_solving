# Adv 주식거래

T = int(input())
for test in range(1, T + 1):
    seed, M = list(map(int, input().split()))  # 시드액, 매달 추가 투자 금액
    N, L = list(map(int, input().split()))  # 종목 수, 개월 수

    stock = [list(map(int, input().split())) for _ in range(N)]
    # print(seed, M)
    # print(N, L)
    # print(stock)
    deposit = seed - M
    bought = []  # 종목, 수량
    for i in range(0, L):
        # 일단 이번달 가용 금액
        deposit += M

        # print(i, deposit, bought)
        if bought:  # 이전 달에 산게 있으면 매도부터 하자
            for item in bought:
                deposit += stock[item[0]][i] * item[1]  # 현재가 * 수량
        # print(deposit)
        buy_list = []  # 종목, 현재가, 예상 수익
        bought = []  # 종목, 수량 (bought reset)
        for n in range(N):
            if stock[n][i] < stock[n][i + 1]:  # 이번달 주가 < 다음달 주가 -> 매수
                buy_list.append((n, stock[n][i], stock[n][i + 1] - stock[n][i]))  # 주식 종목, 현재달 주가, 예상 수익
        # print(buy_list)

        if buy_list:  # 살만한 종목이 있으면
            # 예상 수익이 높은 순서대로 정렬하고
            # 예상 수익이 높은 순서대로, 살 수 있는 최대로 구매
            buy_list.sort(key=lambda x: -x[2])  # 내림차순 정렬
            # print(buy_list)
            for buy in buy_list:
                cnt = 0
                while deposit - buy[1] >= 0:
                    deposit -= buy[1]
                    cnt += 1
                bought.append((buy[0], cnt))
            # print(bought)

    # 마지막 달
    if bought:
        for item in bought:
            deposit += stock[item[0]][L] * item[1]  # 현재가 * 수량
    deposit += M

    benefit = deposit - (seed + L * M)
    print(f'#{test} {benefit}')