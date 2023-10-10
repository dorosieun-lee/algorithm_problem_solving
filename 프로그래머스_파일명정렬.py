# 프로그래머스 파일명 정렬
# 특수문자끼리도 순서가 있어서, head 저장할 때, 특수문자도 포함 시켜야함!

def solution(files):
    answer = []
    my_files = [] # 인덱스, head, number 담을 리스트
    for i, file in enumerate(files):
        for j in range(len(file)):
            if file[j].isdigit():
                head_end = j
                while j < len(file) and file[j].isdigit():
                    j += 1
                number_end = j
                break
        head = file[:head_end].lower()
        number = int(file[head_end:]) if number_end == len(file) else int(file[head_end:number_end])
        my_files.append((i, head, number))
        my_files.sort(key=lambda x: (x[1], x[2])) # 이 부분이 키 포인트! 1번 요소로 먼저 정렬하고, 같으면 2번 요소로 정렬
    for idx, _, _ in my_files:
        answer.append(files[idx])
    return answer

# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files = ["img12", "img10", "img02", "img1", "IMG01", "img2"]
print(solution(files))