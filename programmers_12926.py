# 221122
# 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''

    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    for element in s:
        if element == ' ':
            answer += element
        elif element in u:
            changed_index = u.index(element) + n
            if changed_index >= len(u):
                answer += u[changed_index - len(u)]
            else:
                answer += u[changed_index]
        elif element in l:
            changed_index = l.index(element) + n
            if changed_index >= len(l):
                answer += l[changed_index - len(l)]
            else:
                answer += l[changed_index]

    return answer


print(solution("AB", 1))
