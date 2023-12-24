# 231224
# [PGS] 2차원으로 만들기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])

    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
