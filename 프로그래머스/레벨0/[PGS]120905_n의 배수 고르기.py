# 230820
# [PGS] n의 배수 고르기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):

    # 나의 풀이
    '''
    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer
    '''

    # 다른 사람 풀이 1
    # filter() 함수와 lambda 함수 사용
    # filter(조건 함수, 순회 가능한 데이터) => return type이 filter이므로 list() 함수 사용
    # return list(filter(lambda num: (num % n) == 0, numlist))

    # 다른 사람 풀이 2
    # list comprehension 사용 => Pythonic Code
    return [num for num in numlist if (num % n) == 0]


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5, [1, 9, 3, 10, 13, 5]))
print(solution(12, [2, 100, 120, 600, 12, 12]))
