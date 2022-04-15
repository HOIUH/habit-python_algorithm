# 20220415
# 평균
# https://www.acmicpc.net/problem/1546

subject_cnt = int(input())

subject_score = list(map(int, input().split()))

#print('subject_score: ', subject_score)

raw_max = max(subject_score)

new_score = 0
for i in range(subject_cnt):
    new_score += subject_score[i]/raw_max*100

new_avg = new_score/subject_cnt
print(new_avg)

