# 20220521
# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

# 다른 풀이 1
def solution(array, commands):
    # map(함수, 리스트)
    # list(map(lambda x: x ** 2, range(5)))   # 파이썬 3에선 list 명시해줘야 결과가 list로 나옴
    return list(map(lambda c: sorted(array[c[0]-1:c[1]])[c[2]-1], commands))

'''
# 다른 풀이 2 
def solution(array, commands):
    answer = []
    
    # 2차원 배열인 commands
    # 아래 for문처럼 사용하면 각 요소에 접근하여 배열 요소를 이루는 값들을 i, j, k에 담음  
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
    
# 내 풀이
def solution(array, commands):
    answer = []

    for command in commands:
        new_arr = array[command[0] - 1:command[1]]
        new_arr.sort()
        answer.append(new_arr[command[2] - 1])

    return answer
'''

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

