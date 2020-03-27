from typing import List


# 1. 首先把nums排序
# 2. 遍历nums， if nums[i] > 0; 说明后续没有三数的和等于0；， 在遍历nums时跳过重复的数字
#       left = i + 1, right = len(nums) - 1
#       sum = nums[i] + nums[left] + nums[right]
#           if sum == 0, left += 1 right -= 1 且跳过相等的值，
#           elif sum < 0, 说明nums[left]太小， left += 1
#           elif sum > 0, 说明nums[right]太大， right -= 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                return res
            if idx > 0 and num == nums[idx-1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum == 0:
                    res.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1; right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
