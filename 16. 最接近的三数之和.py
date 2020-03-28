from typing import List

# 解题思路与15题， 三数之和 类似
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        three_sum = -999999
        nums.sort()
        for idx, num in enumerate(nums):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                temp_sum = num + nums[left] + nums[right]
                three_sum = temp_sum if abs(target-temp_sum) < abs(target-three_sum) else three_sum
                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left += 1
                else:
                    return temp_sum
        return three_sum


if __name__ == '__main__':
    nums = [9, 2, -1, 4]
    nums.sort()
    print(nums)