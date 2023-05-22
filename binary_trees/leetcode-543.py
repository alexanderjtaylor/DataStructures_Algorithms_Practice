

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, node):
#         res = 0
#         def height(node):
#             nonlocal res
#             if node is None:
#                 return -1
#             else:
#                 left = height(node.left)
#                 right = height(node.right)
#                 res = max(res, 2 + left + right)
#             return 1 + max(left, right)
#         height(node)
#         return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0  # variable to store the maximum diameter found so far
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)  # update ans if new diameter is found
            return max(left, right) + 1  # return the maximum height of the node
            
        dfs(root)
        return self.ans