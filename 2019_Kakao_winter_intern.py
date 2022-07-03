# 220703
# 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0

    # 내 풀이에서 필요없는 부분을 걷어낸 코드
    bucket = []

    for move in moves:
        for i in range(len(board)):
            target = board[i][move-1]
            if target != 0:
                bucket.append(target)
                board[i][move - 1] = 0

                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop()
                        bucket.pop()
                        answer += 2

                break

    return answer

    # 나의 풀이
    '''
    bucket = []
    for move in moves:
        for i in range(len(board)):
            target = board[i][move - 1]
            if target == 0:
                pass
            else:
                if not bucket:  # if bucket is empty
                    bucket.append(target)
                else:
                    if bucket[-1] == target:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(target)

                board[i][move - 1] = 0
                break
    return answer
    '''

'''
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
'''