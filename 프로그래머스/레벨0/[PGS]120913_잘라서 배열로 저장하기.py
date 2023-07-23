# 230723
# [PGS] 잘라서 배열로 저장하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):

    # 나의 풀이
    '''
    answer = []

    for i in range(len(my_str)):
        if (i % n) == 0:
            answer.append(my_str[i:i+n])    # 슬라이싱은 초과해도 에러나지 않음

    return answer
    '''

    # 다른 사람 풀이
    # List Comprehension 과 range 증가폭 사용한 풀이
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]


print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))
