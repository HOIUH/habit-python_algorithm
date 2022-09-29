# 220929
# 2019 KAKAO BLIND RECRUITMENT > 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter

def solution(N, stages):
    answer = []
    total_user_cnt = len(stages)
    stages = Counter(stages)

    fail_rate_dict = {0: []}
    for i in range(N):
        stage_no = i+1
        if stage_no not in stages:
            fail_rate_dict[0].append(stage_no)
        else:
            stage_user_cnt = stages[i+1]
            fail_rate = stage_user_cnt / total_user_cnt
            total_user_cnt -= stage_user_cnt

            if fail_rate not in fail_rate_dict:
                fail_rate_dict[fail_rate] = []
            fail_rate_dict[fail_rate].append(stage_no)

    s = sorted(fail_rate_dict.items(), reverse=True)
    print(s)

    for elem in s:
        answer.append(elem[1])

    return sum(answer, [])

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))