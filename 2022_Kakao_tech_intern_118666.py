# 221013
# 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    type_nm = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    type_cnt = [0] * 8

    for i in range(len(survey)):
        survey_element = survey[i]
        if choices[i] < 4:
            type_cnt[type_nm.index(survey_element[0])] += 4 - choices[i]
        elif choices[i] > 4:
            type_cnt[type_nm.index(survey_element[1])] += choices[i] - 4

    for j in range(0, len(type_cnt), 2):
        if type_cnt[j] >= type_cnt[j+1]:
            answer += type_nm[j]
        else:
            answer += type_nm[j+1]

    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
# types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
