class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, tree):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if tree is None:
            return tree

        temp = tree.left
        tree.left = tree.right
        tree.right = temp
        self.invertTree(tree.left)
        self.invertTree(tree.right)

        return tree
