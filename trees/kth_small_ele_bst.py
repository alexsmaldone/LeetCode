# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        order = []

        def dfs(node):
            if node:
                dfs(node.left)
                order.append(node.val)
                dfs(node.right)
        dfs(root)
        return order[k-1]


    # ITERATIVE SOLUTION
#     stack = []
#         curr = root

#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             k -= 1
#             if k == 0:
#                 return curr.val
#             curr = curr.right
