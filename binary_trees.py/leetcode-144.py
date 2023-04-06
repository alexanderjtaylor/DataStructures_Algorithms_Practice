

# binary tree preorder traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# class Solution:
#     def preorderTraversal(self, node):
#         if node is None:
#             return []
#         else:
#             res = []
#             res.append(node.val)
#             res+=self.preorderTraversal(node.left)
#             res+=self.preorderTraversal(node.right)
#         return res
    
    
# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    printPreorder(root)