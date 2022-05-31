# 220531
# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums1 m 이후 인덱스 삭제하고
        # nums1 와 nums2 합친 뒤 sort()
        # 답은 나오지만 출제자가 의도한 답인가?
        del nums1[m:]

        nums1 += nums2

        nums1.sort()

        '''
        # 오답
        # 아래 코드 결과: [1, 2, 5, 6, 2, 3]
        if len(nums1) > m: nums1 = nums1[:m]
        if len(nums2) > n: nums2 = nums2[:n]

        if m == 0:
            nums1 = nums2
        elif n > 0:
            for i in range(m):
                if nums1[i] < nums2[0]:
                    nums1.insert(i+1, nums2.pop(0))   
        '''