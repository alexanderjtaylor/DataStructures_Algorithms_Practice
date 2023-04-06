

# binary tree postorder traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# class Solution:
#     def postorderTraversal(self, node):
#         if node is None:
#             return []
#         else:
#             res = []
#             res+=self.postorderTraversal(node.left)
#             res+=self.postorderTraversal(node.right)
#             res.append(node.val)
#         return res

# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)
 
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    printPostorder(root)