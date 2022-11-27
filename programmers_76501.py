# 221127
# 월간 코드 챌린지 시즌2 > 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))

'''
    # 나의 풀이
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
'''


print(solution([4, 7, 12], [True, False, True]))
