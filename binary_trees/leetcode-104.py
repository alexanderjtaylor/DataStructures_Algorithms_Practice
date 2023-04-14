

class Solution:
    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))