class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)       # Visit the root node
            preorder(node.left)        # Traverse left subtree
            preorder(node.right)       # Traverse right subtree

        preorder(root)
        return res
