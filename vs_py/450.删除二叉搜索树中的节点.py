#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key == root.val:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            else:
                node = root.left
                while node.right is not None:
                    node = node.right
                
                root.val = node.val
                root.left = self.deleteNode(root.left, node.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root
    
    # def delt(self, root):
    #     if root.left is None and root.right is None:
    #         root = None
    #     elif root.left is not None and root.right is None:
    #         root.val = root.left.val
    #         root.left = root.left.left
    #         root.right = root.left.right
    #     elif root.right is not None and root.left is None:
    #         root= root.right
    #         root.left = root.right.left
    #         root.right = root.right.right
    #     else:
    #         node = root.left
    #         while node is not None:
    #             node = root.right
    #         root.val = node.val
    #         self.deleteNode(root, root.val)


        
# @lc code=end

