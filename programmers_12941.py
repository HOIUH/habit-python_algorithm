# 221025
# 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    while len(A):
        a = A.pop()
        b = B.pop()
        answer += a * b

    return answer


print(solution([1, 2], [3, 4]))
