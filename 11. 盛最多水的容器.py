from typing import List


class Solution:
    # 思路双指针， left, right 分别指向height列表的两侧
    # 那一侧的数值小移动那一侧， 如果两侧数值同样大， 则同时移动
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1; right -= 1
        return max_area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print(s.maxArea(height))
