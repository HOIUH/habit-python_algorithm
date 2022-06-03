# 220603
# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 중복값 없앤 후 nums 에 바로 할당하면 원하는 답 나오지 않음
        # nums = list(set(nums))

        k = len(set(nums))
        nums[0:k] = list(set(nums))
        del nums[k:]
        nums.sort()

