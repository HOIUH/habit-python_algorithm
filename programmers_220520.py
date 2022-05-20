# 220520
# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 리스트를 큐처럼 사용
# https://www.daleseo.com/python-queue/

def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:    # IndexError: list index out of range 방지 위함
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer

'''
import math

def solution(progresses, speeds):
    answer = []
    end_list = []

    for i in range(len(progresses)):
        end = math.ceil((100-progresses[i])/speeds[i])
        end_list.append(end)

    for j in range(len(end_list)):
        if end_list[j] == -1 :
            continue
        num = 1

        if j == len(end_list)-1:
            answer.append(num)
            break

        for k in range(j+1, len(end_list)):
            if end_list[j] < end_list[k]:
                answer.append(num)
                break
            else:
                num += 1
                end_list[k] = -1
                if k == len(end_list)-1:
                    answer.append(num)
                    break
    return answer
'''