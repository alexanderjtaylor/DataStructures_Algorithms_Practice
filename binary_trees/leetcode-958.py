

class Solution:
    def isCompleteTree(self, root) -> bool:
        nodes = [root]
        is_none = False
        for node in nodes:
            if not node:
                is_none = True
                continue
            if is_none:
                return False
            nodes.append(node.left)
            nodes.append(node.right)
        return True