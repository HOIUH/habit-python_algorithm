# 230627
# [PGS] 캐릭터의 좌표 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    answer = [0, 0]
    x_limit, y_limit = board[0] // 2, board[1] // 2

    for k in keyinput:
        if k == 'left' and answer[0] > -x_limit:
            answer[0] -= 1
        elif k == 'right' and answer[0] < x_limit:
            answer[0] += 1
        elif k == 'down' and answer[1] > -y_limit:
            answer[1] -= 1
        elif k == 'up' and answer[1] < y_limit:
            answer[1] += 1

    return answer

    # 다른 사람 풀이
    '''
    x, y = 0, 0
    x_limit, y_limit = board[0] // 2, board[1] // 2
    move = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1), }

    for k in keyinput:
        dx, dy = move[k]    # 딕셔너리 key로 value값 get
        if abs(x+dx) > x_limit or abs(y+dy) > y_limit:
            continue
        else:
            x, y = x+dx, y+dy

    return [x, y]
    '''
