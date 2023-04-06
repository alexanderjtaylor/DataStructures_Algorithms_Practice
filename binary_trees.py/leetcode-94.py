
# binary tree inorder traversal
class Solution:
    def inorderTraversal(self, node):
        if node is None:
            return []
        else:
            res = []
            res+=self.inorderTraversal(node.left)
            res.append(node.val)
            res+=self.inorderTraversal(node.right)
        return res