# 220731
# Design Parking System
# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big, medium, small):
        self.slot_list = [big, medium, small]

    # 내 풀이에서 수행시간 단축한 코드
    def addCar(self, carType):
        self.slot_list[carType - 1] -= 1
        return self.slot_list[carType - 1] >= 0

'''
# 나의 풀이
class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.slot_list = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slot_list[carType - 1]:
            self.slot_list[carType - 1] -= 1
            return True
        else:
            return False
'''

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
