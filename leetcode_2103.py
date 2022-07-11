# 220711
# Rings and Rods
# https://leetcode.com/problems/rings-and-rods/

'''
1. Python Dictionary Type
2. dictionary[key].add(value)
3. for v in dictionary.values()
for k, v in dictionary.items()
for i, (k, v) in enumerate(dictionary.items())
'''

class Solution:
    def countPoints(self, rings: str) -> int:

        rods_dict = {}

        for i in range(1, len(rings), 2):
            key = rings[i]
            value = rings[i - 1]

            # 딕셔너리에 key 없으면 value를 set 형식으로 갖는 key 추가
            if key not in rods_dict:
                rods_dict[key] = set()

            rods_dict[key].add(value)

        result = 0
        for value in rods_dict.values():  # 딕셔너리에서 value들만 뽑아서 for문 수행
            if len(value) == 3:
                result += 1

        return result