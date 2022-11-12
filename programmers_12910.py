# 221112
# 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

'''
1. A or B
- A, B 둘 다 참이면 A 출력
- A, B 둘 다 거짓이면 B 출력
- A, B 둘 중에 하나만 참이면 참인 값을 출력
'''

def solution(arr, divisor):
    # or 사용한 풀이
    return sorted([element for element in arr if (element % divisor) == 0]) or [-1]

# 나의 풀이
'''
    answer = []
    for element in arr:
        if (element % divisor) == 0:
            answer.append(element)
    if answer:
        return sorted(answer)
    else:
        return [-1]
'''

print(solution([5, 9, 7, 10], 5))