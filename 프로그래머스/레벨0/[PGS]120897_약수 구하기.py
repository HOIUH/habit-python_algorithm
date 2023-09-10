# 230910
# [PGS] 약수 구하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120897

def solution(n):

    # 나의 풀이
    # 제곱근과 집합을 사용 => 매개변수 값 커졌을 때 훨씬 빠름
    answer = set()
    sqrt_val = int(n ** 0.5)

    for i in range(1, sqrt_val + 1):
        share, remainder = divmod(n, i)
        if remainder == 0:
            answer.add(i)
            answer.add(share)

    return sorted(list(answer))

    # 다른 사람 풀이
    # filter(조건 함수, 순회 가능한 데이터)
    # return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]


print(solution(24))
print(solution(29))
