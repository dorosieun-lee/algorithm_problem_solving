# 프로그래머스 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["12","123","1235","567","88"]
phone_book = ["123","456","789"]
print(solution(phone_book))