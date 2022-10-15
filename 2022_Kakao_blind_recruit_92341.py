# 221015
# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from datetime import datetime
import math

# fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
def solution(fees, records):
    answer = []
    # records 공백 기준으로 split
    car_dict = {}
    for record in records:
        record = record.split(' ')
        car_no = record[1]
        if car_dict.get(car_no):
            car_dict[car_no].append(record[0])
        else:
            car_dict[car_no] = [record[0]]

    for k, v in car_dict.items():
        if len(v) % 2:  # 입출차 개수가 홀수개면
            car_dict[k].append('23:59')

        total_time = 0
        for i in range(0, len(v), 2):
            total_time += (datetime.strptime(v[i+1], '%H:%M')-datetime.strptime(v[i], '%H:%M')).total_seconds()/60

        if total_time > fees[0]:
            car_dict[k] = fees[1]+math.ceil((total_time-fees[0])/fees[2])*fees[3]
        else:
            car_dict[k] = fees[1]

    sorted_temp = sorted(car_dict.items())
    for elem in sorted_temp:
        answer.append(elem[1])

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
