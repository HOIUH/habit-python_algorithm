# 220915
# 완전탐색 > 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

'''
1. for idx,element in enumerate(list)
'''

def solution(answers):
    # enumerate 사용한 풀이
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == (idx%5)+1:
            score[0] += 1
        if answer == pattern2[idx%8]:
            score[1] += 1
        if answer == pattern3[idx%10]:
            score[2] += 1

    max_score = max(score)
    for idx, s in enumerate(score):
        if s == max_score:
            result.append(idx+1)

    return result

    # 나의 풀이
    '''
    result = []
    first, second, third = 0, 0, 0
    second_list = [2,1,2,3,2,4,2,5]
    third_list = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        answer = answers[i]
        if answer == (i%5)+1:
            first += 1

        if answer == second_list[(i%8)]:
            second += 1

        if answer == third_list[(i%10)]:
            third += 1

    max_cnt = max(first, second, third)
    if first == max_cnt: result.append(1)
    if second == max_cnt: result.append(2)
    if third == max_cnt: result.append(3)

    return result
    '''

answers = [1,3,2,4,2]
print(solution(answers))