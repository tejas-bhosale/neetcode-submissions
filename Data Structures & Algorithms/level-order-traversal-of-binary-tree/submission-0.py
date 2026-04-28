# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            q_len = len(q)
            temp = []
            for i in range(q_len):
                curr = q.popleft()
                if not curr:
                    continue
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                temp.append(curr.val)
            res.append(temp)
        return res

        