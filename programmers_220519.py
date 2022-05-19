# 20220519
# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

# python heapq 모듈 사용법
# https://www.daleseo.com/python-heapq/

import heapq

def solution(scoville, K):
    answer = 0

    # 기존 리스트를 힙으로 변환
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break

        # heap[0]에 가장 작은 원소가 있다고 해서, heap[1]에 두번째 작은 원소가 있다는 보장 없음
        # heappop() 함수로 가장 작은 원소 삭제할때마다 이진 트리 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문
        # 따라서, 두번째로 작은 원소 얻으려면 heap[1]로 접근하면 안된다!!
        first_min = scoville[0]
        heapq.heappop(scoville)
        second_min = scoville[0]
        heapq.heappop(scoville)
        new_s = first_min + (second_min * 2)
        heapq.heappush(scoville, new_s)
        answer += 1

    return answer