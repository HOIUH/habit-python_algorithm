# 220922
# 스택/큐 > 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        val = arr[i]
        if not answer:
            answer.append(val)
        else:
            if arr[i-1] != val:
                answer.append(val)
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))