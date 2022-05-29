# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                levels.append(level)
        return levels

        # ITERATIVE SOLUTION
#         levels = []
#         if not root:
#             return levels

#         def helper(node, level):
#             if len(levels) == level:
#                 levels.append([])
#             levels[level].append(node.val)
#             if node.left: helper(node.left, level + 1)
#             if node.right: helper(node.right, level + 1)

#         helper(root, 0)
#         return levels
