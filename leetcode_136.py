# 220807
# Single Number
# https://leetcode.com/problems/single-number/

# You must implement a solution
# with a linear runtime complexity
# and use only constant extra space

'''
1. lambda 함수는 콜론(:) 기준으로 좌측에 입력 파라미터를, 우측에 return 할 값을 입력
    주로 map, filter, reduce 함수와 같이 씀
2. from functools import reduce
    reduce() => 인자를 누적으로 적용하여 결과를 반환
3. from operator import xor 또는 ^
    두 수가 다른 경우 1 반환
'''

from collections import Counter
from functools import reduce
from operator import xor

class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums) -> int:

        # reduce() => 인자를 누적으로 적용하여 결과를 반환
        return reduce(lambda total, el: total ^ el, nums)

        # operator의 xor 사용
        # return reduce(xor, nums)

        # 나의 풀이
        # return Counter(nums).most_common()[-1][0]

n = [4,1,2,1,2]
a = Solution()
print(a.singleNumber(n))
