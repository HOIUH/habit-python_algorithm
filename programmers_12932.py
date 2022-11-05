# 221105
# 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    # 풀이 1
    # map()과 reversed()
    return list(map(int, reversed(str(n))))

    # 풀이 2
    # List Comprehension
    # return [int(x) for x in str(n)[::-1]]

'''
    # 풀이 3
    # str[::-1] 사용
    answer = []
    n = str(n)[::-1]
    for element in n:
        answer.append(int(element))
    return answer
'''

print(solution(12345))
