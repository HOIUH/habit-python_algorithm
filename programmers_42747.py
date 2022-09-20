# 220920
# 정렬 > H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    h = len(citations)
    while h:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
            if cnt >= h:
                return h
        h -= 1
    return 0

citations = [3, 0, 6, 1, 5]
print(solution(citations))