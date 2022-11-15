# 221115
# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    zero_cnt, min_cnt = 0, 0

    for num in lottos:
        if num == 0:
            zero_cnt += 1
        elif num in win_nums:
            min_cnt += 1

    max_cnt = min_cnt + zero_cnt

    # 나의 풀이를 더 간단하게 바꾼 코드
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[max_cnt], rank[min_cnt]]

    # 나의 풀이
    '''
    answer = []
    
    if max_cnt >= 2:
        answer.append(7-max_cnt)
    else:
        answer.append(6)

    if min_cnt >= 2:
        answer.append(7-max_cnt)
    else:
        answer.append(6)
    '''

    return answer

