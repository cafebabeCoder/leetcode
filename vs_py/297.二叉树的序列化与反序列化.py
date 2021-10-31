#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
class Codec:
    res = []
    END=-1001

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        if root is None:
            return self.res
        for_visit = [root]
        while len(for_visit) > 0:
            first = for_visit.pop(0)
            if first is None:
                self.res.append(self.END)
            else:
                self.res.append(first.val)
                for_visit.append(first.left)
                for_visit.append(first.right)
            
        return self.res



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if len(data) == 0 :
            return None
        
        root = TreeNode(data[0])
        for_visit = [root]
        i = 1
        while i < len(data):
            p = for_visit.pop(0)
            left = data[i]
            i += 1
            if left == self.END:
                p.left = None
            else:
                p.left = TreeNode(left)
                for_visit.append(p.left)
            right = data[i]
            i+= 1
            if right == self.END:
                p.right = None
            else:
                p.right = TreeNode(right)
                for_visit.append(p.right)
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

