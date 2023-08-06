# 230806
# [PGS] 7의 개수 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    # 나의 풀이
    '''
    answer = 0

    for e in array:
        str_e = str(e)                  # 1. array 요소 int -> str 형변환
        for i in range(len(str_e)):     # 2. 문자열 length만큼 루프 돌면서 '7' 발견하면 answer 증가
            if str_e[i] == '7':
                answer += 1

    return answer
    '''

    # 다른 사람 풀이 1 => BEST!!
    # str(list) 형변환하면 '[7, 77]' 이런식으로 괄호까지 값으로 들어감
    # count() => 문자열, 리스트 내에서 찾고 싶은 문자 개수 반환
    return str(array).count('7')

    # 다른 사람 풀이 2
    # map(함수, 리스트) 순서로 사용
    # return ''.join(map(str, array)).count('7')


print(solution([7, 77, 17]))
print(solution([10, 29]))
