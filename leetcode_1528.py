# 220716
# Shuffle String
# https://leetcode.com/problems/shuffle-string/

'''
1. enumerate
2. join() => list to string
3. zip()
4. sorted()
'''

class Solution:
    # def restoreString(self, s: str, indices: List[int]) -> str:
    def restoreString(self, s, indices) -> str:

        # enumerate와 join 사용
        result = [None] * len(s)
        for index, value in enumerate(indices):
            result[value] = s[index]
        result = ''.join(result)

        # 나의 풀이
        # zip과 sorted, join 사용
        '''
        zipped = zip(indices, s)
        sorted_zipped = sorted(zipped, key=lambda x: x[0])
        result = ''.join([z[1] for z in sorted_zipped])
        '''

        return result

'''
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
a = Solution()
print(a.restoreString(s, indices))
'''