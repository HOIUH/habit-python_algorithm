# 230730
# [PGS] 연속된 수의 합 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    # 나의 풀이
    # 몫과 나머지 이용
    '''
    answer = []
    share, remainder = divmod(total, num)

    if remainder == 0:
        x = (num-1) // 2
        for i in range(share-x, share+x+1):
            answer.append(i)
    else:
        for i in range(share-remainder+1, share+remainder+1):
            answer.append(i)

    return answer
    '''

    # 다른 사람 풀이
    # 몫과 num//2 이용
    if num % 2 == 0:
        return list(range(total//num - num//2 + 1, total//num + num//2 + 1))
    else:
        return list(range(total//num - num//2, total//num + num//2 + 1))


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))
