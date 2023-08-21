# 파일명과 경로 적절히 수정
f1 = 'C:/Users/SSAFY/Desktop/For_algorithm/for_test/output_Me.txt'
f2 = 'C:/Users/SSAFY/Desktop/For_algorithm/for_test/output_ANS.txt'
ip_f = 'C:/Users/SSAFY/Desktop/For_algorithm/for_test/input.txt'

with open(f1, mode='r', encoding='utf-8') as f:
    data1 = f.readlines()
with open(f2, mode='r', encoding='utf-8') as f:
    data2 = f.readlines()
with open(ip_f, mode='r', encoding='utf-8') as f:
    input_data = f.readlines()

for i in range(len(data1)):
    if data1[i] != data2[i]:
        print('테스트케이스 번호:', i+1)
        print('[input data]')
        print(input_data[i*3 + 1]) # input data 형식에 따라 적절히 수정
        print(input_data[i*3 + 2])
        print(input_data[i*3 + 3])