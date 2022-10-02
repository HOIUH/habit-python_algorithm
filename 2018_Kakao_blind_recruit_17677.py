# 221002
# 2018 KAKAO BLIND RECRUITMENT > [1차] 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

# 두 글자씩 끊어서 다중집합의 원소로 만들기
# 영문자 글자 쌍만 유효, 대소문자 차이 무시 => 유효하지 않은 다중집합 원소 삭제하기
# 자카드 유사도 출력 => int(교집합 개수 / 합집합 개수 * 65536)

from collections import Counter

def solution(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    inter = sum((Counter(str1) & Counter(str2)).values())
    union = sum((Counter(str1) | Counter(str2)).values())

    j = 1 if not union else inter / union
    return int(j * 65536)

# 나의 풀이
'''
import re

def make_set_list(str0):
    set_list = []
    p = re.compile('[a-zA-Z]{2}')

    for i in range(len(str0) - 1):
        element = str0[i:i + 2]
        if p.match(element) is not None:
            set_list.append(element.upper())

    return set_list

def solution(str1, str2):
    sl1, sl2 = make_set_list(str1), make_set_list(str2)
    mn, mx = min(sl1, sl2), max(sl1, sl2)
    print(mn, mx)
    len_mn, len_mx = len(mn), len(mx)
    print(len_mn, len_mx)
    intersection = 0

    for elem in mn:
        if elem in mx:
            mx.remove(elem)
            intersection += 1
    union = len_mn+len_mx-intersection

    return int(intersection/union*65536) if not union else 65536
'''

# str1, str2 = 'aa1+aa2', 'AAAA12'
# str1, str2 = 'FRANCE', 'french'
# str1, str2 = 'handshake', 'shake hands'
str1, str2 = 'E=M*C^2', 'e=m*c^2'
print(solution(str1, str2))

