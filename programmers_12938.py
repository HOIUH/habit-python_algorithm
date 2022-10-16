# 221016
# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

# 비슷한 값들을 곱했을 때 결과가 가장 크게 나옴
# s를 n으로 나눈 몫에 나머지 개수만큼 1씩 더해준 숫자들의 집합이 최고의 집합임
def solution(n, s):
    answer = []
    share, remainder = divmod(s, n)

    # 아래 주석처리 된 부분을 위에서 체크하는 걸로 변경
    if share == 0:
        return [-1]

    answer += [share] * (n - remainder)
    answer += [share + 1] * remainder

    '''
    if answer[0] == 0:
        answer = [-1]
    '''

    return answer


print(solution(2, 9))
