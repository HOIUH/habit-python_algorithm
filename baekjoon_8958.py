# 20220416
# OX퀴즈
# https://www.acmicpc.net/problem/8958

test_cnt = int(input())

for _ in range(test_cnt):
    quiz_result = input()

    score = 0
    sum_score = 0

    for i in range(len(quiz_result)):
        if quiz_result[i] == 'O':
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)

'''
# 테스트 케이스를 한번에 입력받고 결과값을 한번에 출력하는 경우
# O 점수를 score_list에 저장해놓고 마지막에 한번에 sum 값 출력
quiz_result = []
for i in range(test_cnt):
    quiz_result.append(input())

for j in range(test_cnt):
    score = 0
    score_list = []
    for k in range(len(quiz_result[j])):
        if quiz_result[j][k] == 'O':
            score += 1
            score_list.append(score)
        else:
            score = 0
    
    print(sum(score_list))
'''