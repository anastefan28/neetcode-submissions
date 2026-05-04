# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for i, value in enumerate(inorder):
            inorder_index[value] = i

        self.preorder_pos = 0
        
        def dfs(left, right):
            if left > right:
                return None
            root_value = preorder[self.preorder_pos]
            self.preorder_pos += 1

            root = TreeNode(root_value)
            mid = inorder_index[root_value]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)

