class Solution:
    def romanToInt(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        ans = 0
        if s.find('CM') != -1:
            ans -= 200
        if s.find('CD') != -1:
            ans -= 200
        if s.find('XC') != -1:
            ans -= 20
        if s.find('XL') != -1:
            ans -= 20
        if s.find('IX') != -1:
            ans -= 2
        if s.find('IV') != -1:
            ans -= 2
        for c in s:
            if c == 'M':
                ans += 1000
            elif c == 'D':
                ans += 500
            elif c == 'C':
                ans += 100
            elif c == 'L':
                ans += 50
            elif c == 'X':
                ans += 10
            elif c == 'V':
                ans += 5
            elif c == 'I':
                ans += 1
        return ans


class Solution:
    def romanToInt(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        help = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        ans = 0
        for cur, c in enumerate(s):
            if cur == len(s)-1:
                ans += help.get(c)
                break
            if help.get(c) < help.get(s[cur+1]):
                ans -= help.get(c)
            else:
                ans += help.get(c)
        return ans


if __name__ == '__main__':
    pass
