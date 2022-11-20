# 221120
# 2021 KAKAO BLIND RECRUITMENT > 순위 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/72412

import re
from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_ = info[:-1]
        info_score = int(info[-1])

        # info의 모든 가능한 조합 생성하여 각각 info_dict의 key로 저장. value는 score.
        for i in range(5):
            for c in combinations(info_, i):
                temp_key = ''.join(c)
                info_dict[temp_key].append(info_score)

    # value 안 score들 오름차순 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = re.sub('and|-', '', query).split()
        query_ = ''.join(query[:-1])
        query_score = int(query[-1])

        # 찾는 조건이 info_dict에 있는 경우
        if query_ in info_dict:
            scores = info_dict[query_]
            if len(scores):
                # 이진탐색
                # score들 중에서 찾는 점수 이상인 score들의 개수만 세야함
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    elif scores[mid] < query_score:
                        start = mid + 1
                answer.append(len(scores)-start)
        else:
            answer.append(0)

    return answer

# 나의 풀이
# 효율성 체크 실패
'''
import re

def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    query = [re.sub('and', '', q).split() for q in query]

    for query_outer_idx in range(len(query)):
        tmp = 0
        for info_outer_idx in range(len(info)):
            if int(info[info_outer_idx][-1]) >= int(query[query_outer_idx][-1]):
                for inner_idx in range(5):
                    if inner_idx == 4:
                        tmp += 1
                    elif query[query_outer_idx][inner_idx] == '-':
                        pass
                    elif query[query_outer_idx][inner_idx] == info[info_outer_idx][inner_idx]:
                        pass
                    else:
                        break
        answer.append(tmp)

    return answer
'''

x = ["java backend junior pizza 150"
    ,"python frontend senior chicken 210"
    ,"python frontend senior chicken 150"
    ,"cpp backend senior pizza 260"
    ,"java backend junior chicken 80"
    ,"python backend senior chicken 50"]
y = ["java and backend and junior and pizza 100"
    ,"python and frontend and senior and chicken 200"
    ,"cpp and - and senior and pizza 250"
    ,"- and backend and senior and - 150"
    ,"- and - and - and chicken 100"
    ,"- and - and - and - 150"]

print(solution(x, y))
