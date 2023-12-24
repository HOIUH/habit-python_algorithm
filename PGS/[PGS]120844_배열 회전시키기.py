# 231224
# [PGS] 배열 회전시키기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    # 풀이 1
    '''
    answer = []

    if direction == 'right':
        answer.append(numbers[-1])  # Return Type: Integer  => append 사용
        answer += numbers[:-1]      # Return Type: List     => + 연산 사용
    else:
        answer += numbers[1:]
        answer.append(numbers[0])

    return answer
    '''

    # 풀이 2
    # return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

    # 풀이 3
    # deque의 rotate 메소드 사용
    # deque.rotate(양수) => 오른쪽 회전. 시계방향
    # deque.rotate(음수) => 왼쪽 회전. 반시계방향
    from collections import deque

    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)