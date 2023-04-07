

# binary tree inorder traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# class Solution:
#     def inorderTraversal(self, node):
#         if node is None:
#             return []
#         else:
#             res = []
#             res+=self.inorderTraversal(node.left)
#             res.append(node.val)
#             res+=self.inorderTraversal(node.right)
#         return res

 
# A function to do inorder tree traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    printInorder(root)