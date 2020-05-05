import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方式
class Solution_1:
    def helper(self, node: TreeNode, low: float, upper: float) -> bool:
        if node is None:
            return True
        val = node.val
        if val <= low or val >= upper:
            return False
        return self.helper(node.left, low, val) and self.helper(node.right, val, upper)

    def isValidBST(self, root: TreeNode) -> bool:
        max_, min_ = sys.maxsize, -(sys.maxsize - 1)
        return self.helper(root, min_, max_)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s, cur = [], root
        prev = -sys.maxsize
        while cur is not None or len(s):
            if cur is not None:
                s.append(cur)
                cur = cur.left
            else:
                now = s.pop()
                if now.val <= prev:
                    return False
                prev, cur = now.val, now.right
        return True


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    s = Solution()
    print(s.isValidBST(root))
