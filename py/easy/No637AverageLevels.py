# 下次尝试下 栈
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        elements = []
        res = []
        elements.append(root)
        while elements:
            length = len(elements)
            s = 0
            for i in range(length):
                cur = elements.pop(0)
                s = s + cur.val
                if cur.left != None:
                    elements.append(cur.left)
                if cur.right != None:
                    elements.append(cur.right)
            res.append(s / length)
        return res

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

print(Solution().averageOfLevels(a))