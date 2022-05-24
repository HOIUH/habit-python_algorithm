# 20220524
# Array Partition I
# https://leetcode.com/problems/array-partition-i/

# 페어의 min()을 합산했을 때 최대(Argmax)를 만드는 것은 결국 min()이 되도록 커야한다는 뜻
# 뒤에서부터 내림차순으로 집어넣으면 항상 최대 min() 페어를 유지할 수 있다
# 이 문제의 배열 입력값은 항상 2n개일 것이므로 앞에서부터 오름차순으로 집어넣어도 결과는 같다

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 풀이3 파이썬다운 방식
        return sum(sorted(nums)[::2])  # 슬라이싱. [::2] 의미 => 2칸씩 건너뜀

        '''
        # 풀이2 짝수 번째 값 계산
        answer = 0
        # nums.sort(reverse=True)   # sorting by descending order
        nums.sort()

        for i in range(0, len(nums), 2):
            answer += min(nums[i], nums[i+1])

        return answer
        '''