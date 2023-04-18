

class Solution:
    def diameterOfBinaryTree(self, node):
        res = 0
        def height(node):
            nonlocal res
            if node is None:
                return -1
            else:
                left = height(node.left)
                right = height(node.right)
                res = max(res, 2 + left + right)
            return 1 + max(left, right)
        height(node)
        return res