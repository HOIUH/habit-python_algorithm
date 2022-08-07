# 220807
# Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from collections import Counter

class Solution:
    # def targetIndices(self, nums: List[int], target: int) -> List[int]:
    def targetIndices(self, nums, target):

        # sort하지 않고 target보다 작은 값 개수 세서 return값 시작 인덱스로 사용
        lt_count, eq_count = 0, 0
        for n in nums:
            if n < target:
                lt_count += 1
            elif n == target:
                eq_count += 1

        return list(range(lt_count, lt_count + eq_count))

        # 나의 풀이
        '''
        nums.sort()
        result = []

        try:
            f_idx = nums.index(target)
            c_get = Counter(nums).get(target)
            result = list(range(f_idx, f_idx + c_get))
            # for v in range(f_idx, f_idx+c_get):result.append(v)
        except ValueError:
            pass

        return result
        '''

        # sort하지 않지만 수행시간은 가장 오래 걸림
        '''
        counter = Counter(nums)
        smaller = sum(v for k, v in counter.items() if k < target)
        return list(range(smaller, smaller + counter[target]))
        '''

nums = [1,2,5,2,3]
target = 2
a = Solution()
print(a.targetIndices(nums, target))