# 231231
# [PGS] 가위 바위 보 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    # 풀이 1
    '''
    answer = ''
    d = {'2':'0', '0':'5', '5':'2'}
    for e in rsp:
        answer += d[e]
    return answer
    '''

    # 풀이 2
    # join 사용
    '''
    d = {'2':'0', '0':'5', '5':'2'}
    return ''.join(d[e] for e in rsp)
    '''

    # 풀이 3
    # replace 사용
    return rsp.replace('2', 's').replace('0', 'r').replace('5', '2').replace('s', '0').replace('r', '5')