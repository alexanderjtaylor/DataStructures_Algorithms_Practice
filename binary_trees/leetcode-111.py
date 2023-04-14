

class Solution:
    def minDepth(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        elif node.right is None:
            return self.minDepth(node.left) + 1
        elif node.left is None:
            return self.minDepth(node.right) + 1
        else:
            return min(self.minDepth(node.left), self.minDepth(node.right)) + 1