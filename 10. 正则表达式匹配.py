class Solution:
    # 递归版本
    def helper_match(self, s: str, p: str, i: int, j: int) -> bool:
        # 当i或者j
        if i == len(s) or j == len(p):
            # i == len(s) 如果p[j+1]为*， 尝试跳过
            while j + 1 < len(p) and p[j+1] == '*':
                j += 2
            return True if i == len(s) and j == len(p) else False
        if j + 1 < len(p) and p[j+1] == '*':
            zero = self.helper_match(s, p, i, j + 2)
            one = False
            if (not zero) and (p[j] == s[i] or p[j] == '.'):
                one = one or self.helper_match(s, p, i+1, j)
            return zero or one
        else:
            return self.helper_match(s, p, i+1, j+1) if s[i] == p[j] or p[j] == '.' else False

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper_match(s, p, 0, 0)


class Solution:
    # 动态规划
    def isMatch(self, s: str, p: str) -> bool:
        # 只要有一个为空
        if not (len(s) or len(p)):
            return True if s == p else False
        bp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        # 初始化bp第一列
        bp[0][0] = True
        for idx, c in enumerate(p):
            if c == '*':
                bp[idx+1][0] = bp[idx-1][0]

        for idx_s, c_s in enumerate(s):
            for idx_p, c_p in enumerate(p):
                if c_p == '*':
                    if c_s == p[idx_p-1] or p[idx_p-1] == '.':
                        bp[idx_p+1][idx_s+1] = bp[idx_p+1][idx_s] or bp[idx_p-1][idx_s+1]
                    else:
                        bp[idx_p+1][idx_s+1] = bp[idx_p-1][idx_s+1]
                else:
                    if c_p == c_s or c_p == '.':
                        bp[idx_p+1][idx_s+1] = bp[idx_p][idx_s]
        return bp[len(p)][len(s)]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa', 'a*'))
