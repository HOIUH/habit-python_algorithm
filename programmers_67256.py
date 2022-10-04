# 221004
# 2020 카카오 인턴십 > 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''

    # [[1, 2, 3],
    #  [4, 5, 6],
    #  [7, 8, 9],
    #  [*, 0, #]]
    # 위와 같은 이차원 배열 형태로 놓고 푼 풀이

    l_location, r_location = [3, 0], [3, 2]
    for number in numbers:
        if number == 0:
            x, y = 3, 1
        else:
            x, y = (number - 1) // 3, (number + 2) % 3

        if number in [1, 4, 7]:
            l_location = [x, y]
            answer += 'L'
        elif number in [3, 6, 9]:
            r_location = [x, y]
            answer += 'R'
        else:
            l_distance, r_distance = abs(x - l_location[0]) + abs(y - l_location[1]), abs(x - r_location[0]) + abs(y - r_location[1])
            if l_distance < r_distance:
                l_location = [x, y]
                answer += 'L'
            elif l_distance > r_distance:
                r_location = [x, y]
                answer += 'R'
            else:
                tmp = hand[0].upper()
                answer += tmp
                if tmp == 'L':
                    l_location = [x, y]
                else:
                    r_location = [x, y]

    return answer

# numbers, hand, result = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"
numbers, hand, result = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"
# numbers, hand, result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL"

print(solution(numbers, hand))