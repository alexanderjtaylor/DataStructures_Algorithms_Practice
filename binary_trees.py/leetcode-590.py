


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node):
        ans = []
        def postorder(node):
            if node is None:
                return []
            else:
                for i in node.children:
                    postorder(i)
                ans.append(node.val)
        postorder(root)
        return ans
    