class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = [0]

        def maxHeightDifferences(node):
            if not node:
                return 0
            left_depth = maxHeightDifferences(node.left)
            right_depth = maxHeightDifferences(node.right)

            result[0] = max(result[0], abs(left_depth - right_depth))

            return max(left_depth, right_depth) + 1

        maxHeightDifferences(root)
        return result[0] <= 1

#    OTHER SOLUTION
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right
