#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # if len(preorder) == 0:
            # return None
        root = self.builds(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        return root

    def builds(self, preorder, pstart, pend, inorder, istart, iend) -> TreeNode:
        if pstart > pend:
            return None 
        root = preorder[pstart]   

        r = TreeNode(root)
        #  i 是根节点在中序遍历的位置
        i=0
        for idx in range(istart, iend+1, 1):
            if root == inorder[idx]:
                i = idx
                break
        leftsize = i - istart

        left = self.builds(preorder, pstart+1, pstart + leftsize, inorder, istart, i-1)

        right = self.builds(preorder, pstart+leftsize+1, pend, inorder, i+1, iend)
        r.left = left
        r.right = right

        return r

    

# pstart = 0, pend = 4, istart=0, iend=4
# root = preorder[0] = 3
# i = 1
# leftsize = i-istart = 1-0 = 1
# build(preorder, 1, 1, inorder, 0, 0)
# build(preorder, 2, 4, inorder, 2, 4)



# @lc code=end
# s = Solution()
# root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
# n = root
# print(n.left.val)