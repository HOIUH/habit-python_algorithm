# 220925
# 2019 카카오 개발자 겨울 인턴십 > 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

'''
1. Counter.most_common() 리턴값 형식은 List
=> 예) [('111', 2), ('20', 1)]
'''

import re
from collections import Counter

def solution(s):

    # 나의 풀이
    answer = []
    s = re.sub("{|}", "", s).split(",")

    s = Counter(s)
    s_list = s.most_common()

    for elem in s_list:
        answer.append(int(elem[0]))

    return answer

# st = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
st = "{{20,111},{111}}"
print(solution(st))
