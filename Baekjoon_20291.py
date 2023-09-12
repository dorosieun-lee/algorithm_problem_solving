# Baekjoon 20291 파일 정리

N = int(input())
exts_dict = {}
exts_list = set()
for _ in range(N):
    filename = input()
    end = filename.split('.')[1]
    exts_list.add(end)
    if end in exts_dict.keys():
        exts_dict[end] += 1
    else:
        exts_dict[end] = 1

for key in sorted(exts_list):
    print(key, exts_dict[key])

"""
더 짧게

N = int(input())
exts_dict = {}
for _ in range(N):
    end = input().split('.')[1]
    exts_dict[end] = exts_dict[end] + 1 if end in exts_dict.keys() else 1

for key, value in sorted(exts_dict.items()):
    print(key, value)
"""