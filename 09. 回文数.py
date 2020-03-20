class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while (x // div) >= 10:
            div *= 10
        while x != 0:
            left, right = x // div, x % 10    # left为最高位， right为最低位
            if left != right:
                return False
            x = (x - left * div) // 10      # x 去除最高位和最低位
            div //= 100
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1))