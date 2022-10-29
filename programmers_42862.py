# 221029
# 탐욕법(Greedy) > 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    len_lost = len(lost)
    answer = n - len_lost
    lost.sort(); reserve.sort()

    for i in range(len_lost):
        target = lost[i]

        if target in reserve:   # 잃어버렸고 본인이 여분 있음
            reserve.remove(target)
            answer += 1
        elif target - 1 in reserve:     # 잃어버렸고 앞번호 학생이 여분 있음
            reserve.remove(target - 1)
            answer += 1
        elif target + 1 in reserve:     # 잃어버렸고 뒷번호 학생이 여분 있음
            if i == len_lost - 1:       # 잃어버린 마지막 학생
                answer += 1
            elif target + 1 != lost[i + 1]:     # 여분있는 뒷번호 학생은 잃어버리지 않은 경우에만
                reserve.remove(target + 1)
                answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
