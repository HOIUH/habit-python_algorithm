# 220731
# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

'''
1. dictionary의 key/value
2. dictionary 대신 list 사용하면 timeout 발생
'''

# 결과 리스트 출력도 dictionary의 key/value 활용한 풀이
def solution(record):
    answer = []
    pairs = dict()
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for rec in record:
        split_rec = rec.split(' ')
        if split_rec[0] in ['Enter', 'Change']:
            pairs[split_rec[1]] = split_rec[2]

    for rec in record:
        split_rec = rec.split(' ')
        action = split_rec[0]
        uid = split_rec[1]
        if action != 'Change':
            answer.append(pairs[uid]+printer[action])

    return answer

# 나의 풀이
'''
def solution(record):
    answer = []
    pairs = dict()
    for i in range(len(record) - 1, -1, -1):
        split_rec = record[i].split(' ')
        if (split_rec[0] != 'Leave') & (split_rec[1] not in pairs):
            pairs[split_rec[1]] = split_rec[2]

    for rec in record:
        split_rec = rec.split(' ')
        if split_rec[0] == 'Leave':
            answer.append(f'{pairs[split_rec[1]]}님이 나갔습니다.')
        elif split_rec[0] == 'Enter':
            answer.append(f'{pairs[split_rec[1]]}님이 들어왔습니다.')

    return answer
'''
