# 220908
# 해시 > 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter

def solution(nums):
    # 해시 사용하지 않고 set로 종류 개수 구함
    return min(len(nums)/2, len(set(nums)))

# 나의 풀이
# Counter 객체 key 사용
'''
    n = int(len(nums) / 2)
    key_count = len(Counter(nums).keys())

    if n > key_count:
        return key_count
    else:
        return n
'''

nums = [3,1,2,3]
print(solution(nums))