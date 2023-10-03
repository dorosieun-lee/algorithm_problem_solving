# 프로그래머스 오픈채팅방

def solution(record):
    answer = []
    id_n_name = {}
    tmp = []
    for r in record:
        try:
            status, id, name = r.split()
        except ValueError:
            status, id = r.split()
        if status == 'Enter':
            id_n_name[id] = name
            tmp.append((status, id))
        elif status == 'Change':
            id_n_name[id] = name
        else:
            tmp.append((status, id))

    for status, id in tmp:
        if status == 'Enter':
            answer.append(f'{id_n_name[id]}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{id_n_name[id]}님이 나갔습니다.')
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))