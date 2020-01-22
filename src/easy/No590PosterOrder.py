"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        if root.children != None:
            for child in root.children:
                res += self.postorder(child)
        res.append(root.val)
        return res

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 =  Node(8)
a9 =  Node(9)
a10 =  Node(10)
a11 = Node(11)
a12 = Node(12)
a13 = Node(13)
a14 = Node(14)

a1.children = [a2, a3, a4, a5]
a3.children = [a6,a7]
a4.children = [a8]
a7.children = [a11]
a8.children = [a12]
a11.children = [a14]
a5.children = [a9, a10]
a9.children = [a13]

print(Solution().postorder(a1))