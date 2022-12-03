# 221203
# 제일 작은 수 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


print(solution([4, 3, 2, 1]))
print(solution([10]))
