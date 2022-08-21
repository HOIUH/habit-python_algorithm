# 220821
# Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    # def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    def arithmeticTriplets(self, nums, diff: int) -> int:

        # 풀이 1
        seen = set()
        '''
        output = 0
        for num in nums:
            if (num - diff) in seen and (num - diff * 2) in seen:
                output += 1
            seen.add(num)
        return output
        '''
        # 위 주석처리 한 부분을 한 줄로 만든 코드
        return sum(n+diff in nums and n+diff*2 in nums for n in nums)


        '''
        # 풀이 2
        output = 0
        for num in nums:
            if num + diff in nums and num + diff * 2 in nums:
                output += 1
        return output
        '''


