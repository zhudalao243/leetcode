
class Solution:
    def get_next_idx(self, idx, direction, num_rows):
        if num_rows == 1:
            return 0
        if idx == 0 or idx == (num_rows - 1):
            direction = True if idx == 0 else False
        idx = idx + 1 if direction else idx - 1
        return idx, direction

    def convert(self, s: str, numRows: int) -> str:
        all_lst = [[] for i in range(numRows)]  # 创建numRows个列表
        idx, direction = 0, True                # all_lst的下标, 下一个idx的方向， True idx += 1
        for c in s:                             # 遍历s字符串
            all_lst[idx].append(c)
            idx, direction = self.get_next_idx(idx, direction, numRows)
        res = ''
        for lst in all_lst:
            res += (''.join(lst))
        return res


class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        all_lst = [[] for i in range(numRows)]
        i, s_len = 0, len(s)
        idx = 0     # all_lst 的下标
        while i < s_len:
            while idx < numRows and i < s_len:
                all_lst[idx].append(s[i])
                idx, i = idx + 1, i + 1
            idx = numRows - 2
            while idx > 0 and i < s_len:
                all_lst[idx].append(s[i])
                idx, i = idx - 1, i + 1
            idx = 0
        res = ''
        for lst in all_lst:
            res += (''.join(lst))
        return res


if __name__ == '__main__':
    s = Solution()
    s1 = 'AB'
    print(s.convert(s1, 1))