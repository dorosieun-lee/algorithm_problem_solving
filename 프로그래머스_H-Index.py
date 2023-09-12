def solution(citations):
    h = 1
    while True:
        over_h = under_h = 0
        for c in citations:
            if c >= h:
                over_h += 1
            else:
                under_h += 1
        # print(h, over_h, under_h)
        if over_h >= h:
            h += 1
        else:
            break

    answer = h - 1
    return answer