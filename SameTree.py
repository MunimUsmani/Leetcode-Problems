# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both nodes are None → trees/subtrees are identical here
        if not p and not q:
            return True
        
        # 2. Exactly one is None → structures differ
        if not p or not q:
            return False
        
        # 3. Values differ → not the same tree
        if p.val != q.val:
            return False
        
        # 4. Recurse on both left and right children
        return (self.isSameTree(p.left,  q.left) and
                self.isSameTree(p.right, q.right))
