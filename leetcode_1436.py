# 220723
# Destination City
# https://leetcode.com/problems/destination-city/

'''
When paths: List[List[str]]
1. x, y = map(set, zip(*paths))
2. set(path[0] for path in paths)
'''

class Solution:
    def destCity(self, paths) -> str:
        # Time: O(N)
        # Space: O(cities)

        # B is the destination set and A is the start point set
        # B-A gives you the one that corresponding to a destination and then you pop it out of the set

        A, B = map(set, zip(*paths))    # The * in zip for unpacking of the list
        return (B - A).pop()

    '''
    # 나의 풀이
    def destCity(self, paths: List[List[str]]) -> str:
    
        # paths[i][0]을 start_cities에 넣음
        # start_cities = [path[0] for path in paths]
        start_cities = set(path[0] for path in paths)   => set로 만들었을 때가 가장 빠름
        
        # start_citiest에 없는 paths[i][1]가 최종 destination city 
        for path in paths:
            if path[1] not in start_cities:
                return path[1]
    '''

paths = [["B","C"],["D","B"],["C","A"]]
a = Solution()
print(a.destCity(paths))