from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        for i in range(len(nums)):
            if i == 0:
                sum.append(nums[i])
            else:
                sum.append(sum[i-1] + nums[i])
        print(sum)

    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        for i in range(len(nums)):
            sum_list.append(sum(nums[:i+1]))
        return sum_list

if __name__ == 'main':
    Solution().runningSum([1,2,3,4,5])
    Solution().runningSum([2,2,2,2,2])
    Solution().runningSum([1])
    Solution().runningSum([0,0,0,0,0])
    Solution().runningSum([1000,100000,1000000,1000000000,1000000000])