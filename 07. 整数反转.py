

class Solution:
    def reverse(self, x: int) -> int:
        y, rev = abs(x), 0
        max_ = (1 << 31) - 1 if x > 0 else 1 << 31    # 用来判断是否溢出， 最大范围[-2^31, 2^31-1]
        while y != 0:
            rev = rev * 10 + y % 10
            if rev > max_:       # 如果rev>max_, 溢出返回0
                return 0
            y //= 10
        return rev if x > 0 else -rev


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1463847412))

